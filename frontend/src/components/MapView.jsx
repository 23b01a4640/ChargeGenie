import { useEffect, useRef } from "react";
import { loadGoogleMaps } from "../utils/loadGoogleMaps";

export default function MapView({ polyline, stations }) {
  const mapRef = useRef(null);
  const map = useRef(null);
  const routeLine = useRef(null);
  const markers = useRef([]);

  // 🗺️ Init map
  useEffect(() => {
    loadGoogleMaps().then(() => {
      map.current = new window.google.maps.Map(mapRef.current, {
        center: { lat: 20.59, lng: 78.96 },
        zoom: 6,
        mapTypeControl: true,
      });
    });
  }, []);

  // 🧭 Draw route polyline
  useEffect(() => {
    if (!polyline || !map.current) return;

    if (routeLine.current) routeLine.current.setMap(null);

    routeLine.current = new window.google.maps.Polyline({
      path: polyline.map(([lat, lng]) => ({ lat, lng })),
      strokeColor: "#2563EB",
      strokeOpacity: 0.9,
      strokeWeight: 4,
    });

    routeLine.current.setMap(map.current);

    // Auto-fit bounds
    const bounds = new window.google.maps.LatLngBounds();
    polyline.forEach(([lat, lng]) =>
      bounds.extend({ lat, lng })
    );
    map.current.fitBounds(bounds);
  }, [polyline]);

  // 📍 Render stations
  useEffect(() => {
    if (!map.current) return;

    markers.current.forEach(m => m.setMap(null));
    markers.current = [];

    stations.forEach(station => {
      const color =
        station.availability === "available"
          ? "green"
          : station.availability === "busy"
          ? "yellow"
          : "red";

      const marker = new window.google.maps.Marker({
        map: map.current,
        position: { lat: station.lat, lng: station.lng },
        title: station.name,
        icon: {
          url: `http://maps.google.com/mapfiles/ms/icons/${color}-dot.png`,
        },
      });

      const info = new window.google.maps.InfoWindow({
        content: `
          <div style="font-size:13px">
            <strong>${station.name}</strong><br/>
            Distance: ${station.distance_km} km<br/>
            Price: ₹${station.price_per_kwh}/kWh<br/>
            Status: ${station.availability}
          </div>
        `,
      });

      marker.addListener("click", () => info.open(map.current, marker));
      markers.current.push(marker);
    });
  }, [stations]);

  return <div ref={mapRef} className="w-full h-full" />;
}
