def shortlist_stations(stations, vehicle):
    reachable_km = (vehicle["battery_percent"] / 100) * vehicle["range_km"]

    candidates = []

    for s in stations:
        if s.get("distance_km") is None:
            continue

        if s["distance_km"] > reachable_km:
            continue

        if s.get("availability") == "full":
            continue

        candidates.append(s)

    candidates.sort(
        key=lambda x: (
            x["distance_km"],
            x.get("price_per_kwh", 8)
        )
    )

    return candidates[:5]


def generate_explanation(candidates, vehicle):
    if not candidates:
        return "No suitable charging stations found for your current battery level."

    lines = []

    for i, s in enumerate(candidates, start=1):
        lines.append(
            f"{i}. {s['name']} — {s['distance_km']} km from route, "
            f"₹{s.get('price_per_kwh', 8)}/kWh, "
            f"{s.get('availability', 'available')}."
        )

    return (
        "Based on your vehicle range and current battery, these stations are optimal:\n"
        + "\n".join(lines)
    )
