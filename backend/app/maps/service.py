import requests
import polyline
import math
from concurrent.futures import ThreadPoolExecutor

from app.core.config import GOOGLE_MAPS_API_KEY
from app.core.database import db
from app.maps.opencharge import fetch_opencharge_stations
from app.maps.normalizer import normalize_ocm_station


# -----------------------------
# Distance Helpers
# -----------------------------

def haversine(lat1, lon1, lat2, lon2):
    R = 6371000
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)

    a = (
        math.sin(dphi / 2) ** 2
        + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
    )
    return 2 * R * math.atan2(math.sqrt(a), math.sqrt(1 - a))


def min_distance_to_route(point, route):
    return min(
        haversine(point[0], point[1], r[0], r[1]) for r in route
    )


# -----------------------------
# ROUTE (Google Directions ONLY)
# -----------------------------

def get_route(source: str, destination: str):
    url = "https://maps.googleapis.com/maps/api/directions/json"
    params = {
        "origin": source,
        "destination": destination,
        "key": GOOGLE_MAPS_API_KEY,
    }

    res = requests.get(url, params=params, timeout=10).json()

    if res.get("status") != "OK":
        raise Exception("Directions API failed")

    route = res["routes"][0]
    leg = route["legs"][0]

    decoded_polyline = polyline.decode(
        route["overview_polyline"]["points"]
    )

    return {
        "polyline": decoded_polyline,
        "distance_km": leg["distance"]["value"] // 1000,
        "duration_min": leg["duration"]["value"] // 60,
    }


# -----------------------------
# EV STATIONS (OpenChargeMap)
# -----------------------------

def get_ev_stations_along_route(route_points):
    stations = []
    seen = set()

    # sample every ~20 points
    sampled = route_points[::20]

    with ThreadPoolExecutor(max_workers=5) as executor:
        results = executor.map(
            lambda p: fetch_opencharge_stations(p[0], p[1]),
            sampled
        )

    for res in results:
        for raw in res:
            pid = f"ocm_{raw['ID']}"
            if pid in seen:
                continue

            s = normalize_ocm_station(raw)

            # 🛑 SAFETY CHECK
            if not s["lat"] or not s["lng"]:
                continue

            # 📏 distance to route
            dist_km = min_distance_to_route(
                (s["lat"], s["lng"]),
                route_points
            ) / 1000

            # ✅ FIX: realistic corridor (10 km)
            if dist_km > 10:
                continue

            meta = db.stations.find_one({"place_id": pid})

            stations.append({
                **s,
                "distance_km": round(dist_km, 1),
                "price_per_kwh": meta.get("price_per_kwh", 8) if meta else 8,
                "availability": meta.get("availability", "available") if meta else "available",
            })

            seen.add(pid)

    return stations
