import requests
from app.core.config import OPENCHARGE_API_KEY

BASE_URL = "https://api.openchargemap.io/v3/poi/"

def fetch_opencharge_stations(lat: float, lng: float):
    params = {
        "output": "json",
        "latitude": lat,
        "longitude": lng,
        "distance": 10,
        "distanceunit": "KM",
        "maxresults": 20,
        "key": OPENCHARGE_API_KEY,
    }

    res = requests.get(BASE_URL, params=params, timeout=10)

    print("OCM status:", res.status_code)
    print("OCM sample:", res.text[:200])

    if res.status_code != 200:
        return []

    return res.json() or []
