import { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

export default function AdminDashboard() {
  const navigate = useNavigate();
  const { user, loading, logout } = useAuth();

  // 🔐 Route protection
  useEffect(() => {
    if (loading) return;

    if (!user) {
      navigate("/admin/login");
      return;
    }

    if (user.role !== "admin") {
      navigate("/dashboard");
    }
  }, [user, loading, navigate]);

  if (loading) return null;

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <div className="max-w-4xl mx-auto bg-white rounded-xl shadow p-6">
        {/* HEADER */}
        <div className="flex justify-between items-center mb-6">
          <h1 className="text-2xl font-semibold">Admin Dashboard</h1>

          <button
            onClick={() => {
              logout();
              navigate("/admin/login");
            }}
            className="text-sm text-red-600 hover:underline"
          >
            Logout
          </button>
        </div>

        <p className="text-gray-600">
          Manage charging stations, pricing, and availability here.
        </p>
      </div>
    </div>
  );
}
