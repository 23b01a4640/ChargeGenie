import { useEffect, useState } from "react";
import {
  getVehicleProfile,
  saveVehicleProfile,
} from "../services/vehicleApi";

export default function VehicleProfile({ vehicle, setVehicle }) {
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("");

  useEffect(() => {
    const load = async () => {
      try {
        const data = await getVehicleProfile();
        if (data?.range_km) {
          setVehicle({
            range_km: data.range_km,
            battery_percent: data.battery_percent,
          });
        }
      } catch (e) {
        console.error("Failed to load vehicle profile");
      }
    };
    load();
  }, [setVehicle]);

  const handleSave = async () => {
    setLoading(true);
    setMessage("");

    try {
      await saveVehicleProfile(vehicle);
      setMessage("✅ Vehicle profile saved");
    } catch {
      setMessage("❌ Failed to save");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="bg-white p-4 rounded-lg shadow">
      <h3 className="text-lg font-semibold mb-3">🚗 Vehicle Details</h3>

      <input
        type="number"
        placeholder="Range (km)"
        className="w-full mb-3 p-2 border rounded"
        value={vehicle.range_km}
        onChange={(e) =>
          setVehicle({ ...vehicle, range_km: Number(e.target.value) })
        }
      />

      <input
        type="number"
        placeholder="Battery %"
        className="w-full mb-3 p-2 border rounded"
        value={vehicle.battery_percent}
        onChange={(e) =>
          setVehicle({
            ...vehicle,
            battery_percent: Number(e.target.value),
          })
        }
      />

      <button
        onClick={handleSave}
        disabled={loading}
        className="bg-emerald-600 text-white px-4 py-2 rounded"
      >
        {loading ? "Saving..." : "Save"}
      </button>

      {message && (
        <p className="text-sm mt-2 text-gray-600">{message}</p>
      )}
    </div>
  );
}
