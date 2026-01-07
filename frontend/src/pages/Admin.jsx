import { useAuth } from "../context/AuthContext";

export default function Admin() {
  const { user, logout } = useAuth();

  return (
    <div className="min-h-screen bg-gray-50 p-8">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-2xl font-semibold text-gray-800">
          Station Admin Panel
        </h1>

        <button
          onClick={logout}
          className="text-sm text-red-500 hover:underline"
        >
          Logout
        </button>
      </div>

      <div className="bg-white rounded-xl shadow p-6 max-w-xl">
        <h2 className="text-lg font-medium mb-4">My Station</h2>

        <div className="space-y-3 text-gray-700">
          <p>
            <span className="font-medium">Station Name:</span> Not linked yet
          </p>
          <p>
            <span className="font-medium">Status:</span> Available
          </p>
          <p>
            <span className="font-medium">Price per kWh:</span> ₹ —
          </p>
        </div>

        <div className="mt-6 space-y-3">
          <button className="w-full py-2 rounded-lg border border-emerald-600 text-emerald-600 hover:bg-emerald-50">
            Toggle Availability
          </button>

          <button className="w-full py-2 rounded-lg bg-emerald-600 text-white hover:bg-emerald-700">
            Update Price
          </button>
        </div>
      </div>
    </div>
  );
}
