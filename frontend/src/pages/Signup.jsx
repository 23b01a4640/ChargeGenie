import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import AuthCard from "../components/AuthCard";
import { useAuth } from "../context/AuthContext";

const API_BASE = "http://127.0.0.1:8000";

export default function Signup({ role }) {
  const navigate = useNavigate();
  const { login, user, loading } = useAuth(); // ✅ loading added

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [loadingForm, setLoadingForm] = useState(false);
  const [error, setError] = useState("");

  // 🔁 Auto redirect AFTER auth restore
  useEffect(() => {
    if (loading) return; // ✅ IMPORTANT FIX

    if (user?.role === "admin") navigate("/admin");
    if (user?.role === "user") navigate("/dashboard");
  }, [user, loading, navigate]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setLoadingForm(true);

    try {
      const res = await axios.post(`${API_BASE}/auth/signup`, {
        email,
        password,
        role,
      });

      const token = res.data.access_token;
      localStorage.setItem("token", token);

      const meRes = await axios.get(`${API_BASE}/auth/me`, {
        headers: { Authorization: `Bearer ${token}` },
      });

      // ✅ Update global auth state
      login(meRes.data);
    } catch (err) {
      setError(
        err.response?.data?.detail || "Signup failed. Please try again."
      );
    } finally {
      setLoadingForm(false);
    }
  };

  return (
    <AuthCard title={role === "admin" ? "Admin Signup" : "User Signup"}>
      <form onSubmit={handleSubmit} className="space-y-5">
        <div>
          <label className="block text-sm font-medium text-gray-600 mb-1">
            Email
          </label>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
            className="w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-emerald-500"
          />
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-600 mb-1">
            Password
          </label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
            className="w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-emerald-500"
          />
        </div>

        {error && (
          <p className="text-sm text-center text-red-500">{error}</p>
        )}

        <button
          type="submit"
          disabled={loadingForm}
          className="w-full bg-emerald-600 text-white py-2 rounded-lg font-medium hover:bg-emerald-700 disabled:opacity-60"
        >
          {loadingForm ? "Creating account..." : "Create Account"}
        </button>

        <p className="text-sm text-center text-gray-500">
          Already have an account?{" "}
          <span
            onClick={() =>
              navigate(role === "admin" ? "/admin/login" : "/user/login")
            }
            className="text-emerald-600 font-medium cursor-pointer hover:underline"
          >
            Login
          </span>
        </p>

        <p className="text-xs text-center text-gray-400">
          Not you?{" "}
          <span
            onClick={() => navigate("/")}
            className="cursor-pointer hover:underline"
          >
            Go back to role selection
          </span>
        </p>
      </form>
    </AuthCard>
  );
}
