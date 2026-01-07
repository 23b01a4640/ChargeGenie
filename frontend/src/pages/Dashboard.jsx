import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

import MapView from "../components/MapView";
import RecommendationPanel from "../components/RecommendationPanel";
import VehicleProfile from "../components/vehicleProfile";
import { fetchRouteData } from "../services/mapsApi";

export default function Dashboard() {
  const navigate = useNavigate();
  const { user, loading, logout } = useAuth();

  // 🔐 Route protection
  useEffect(() => {
    if (loading) return;

    if (!user) {
      navigate("/user/login");
      return;
    }

    if (user.role !== "user") {
      navigate("/admin");
    }
  }, [user, loading, navigate]);

  const [source, setSource] = useState("");
  const [destination, setDestination] = useState("");
  const [route, setRoute] = useState(null);
  const [stations, setStations] = useState([]);
  const [recommendation, setRecommendation] = useState(null);
  const [loadingRoute, setLoadingRoute] = useState(false);
  const [error, setError] = useState("");

  const [vehicle, setVehicle] = useState({
    range_km: 0,
    battery_percent: 0,
  });

  const handleSearch = async () => {
    setError("");
    setLoadingRoute(true);
    setRecommendation(null);

    try {
      const data = await fetchRouteData(source, destination);
      setRoute(data.route);
      setStations(data.stations);

      const recRes = await fetch("http://127.0.0.1:8000/recommend/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${localStorage.getItem("token")}`,
        },
        body: JSON.stringify({
          source,
          destination,
          stations: data.stations,
          vehicle,
        }),
      });

      const recData = await recRes.json();
      setRecommendation(recData);
    } catch {
      setError("Failed to fetch route or recommendations");
    } finally {
      setLoadingRoute(false);
    }
  };

  if (loading) return null;

  return (
    <div className="flex h-screen bg-gray-100">
      {/* LEFT PANEL */}
      <div className="w-[380px] p-6 bg-white shadow-lg overflow-y-auto">
        {/* HEADER */}
        <div className="flex justify-between items-center mb-4">
          <h2 className="text-xl font-semibold">ChargeGenie</h2>
          <button
            onClick={() => {
              logout();
              navigate("/user/login");
            }}
            className="text-sm text-red-600 hover:underline"
          >
            Logout
          </button>
        </div>

        <input
          className="w-full mb-3 p-2 border rounded"
          placeholder="Source"
          value={source}
          onChange={(e) => setSource(e.target.value)}
        />

        <input
          className="w-full mb-3 p-2 border rounded"
          placeholder="Destination"
          value={destination}
          onChange={(e) => setDestination(e.target.value)}
        />

        <button
          onClick={handleSearch}
          disabled={loadingRoute}
          className="w-full bg-emerald-600 text-white py-2 rounded"
        >
          {loadingRoute ? "Analyzing..." : "Find Charging Stations"}
        </button>

        {error && <p className="text-red-500 mt-3 text-sm">{error}</p>}

        <div className="border-t my-6" />

        <VehicleProfile vehicle={vehicle} setVehicle={setVehicle} />

        <RecommendationPanel recommendation={recommendation} />
      </div>

      {/* MAP */}
      <div className="flex-1">
        <MapView polyline={route?.polyline} stations={stations} />
      </div>
    </div>
  );
}
