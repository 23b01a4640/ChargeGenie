def normalize_ocm_station(raw):
    address = raw.get("AddressInfo", {})
    connections = raw.get("Connections", [])

    power_kw = None
    connector = "Unknown"

    if connections:
        conn = connections[0]
        power_kw = conn.get("PowerKW")
        connector = conn.get("ConnectionType", {}).get("Title", "Unknown")

    return {
        "place_id": f"ocm_{raw['ID']}",
        "name": address.get("Title", "Unknown Station"),
        "lat": address.get("Latitude"),
        "lng": address.get("Longitude"),
        "operator": raw.get("OperatorInfo", {}).get("Title", "Unknown"),
        "power_kw": power_kw,
        "connector": connector,
    }
