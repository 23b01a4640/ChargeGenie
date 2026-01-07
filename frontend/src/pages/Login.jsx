import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import { useAuth } from "../context/AuthContext";
import AuthCard from "../components/AuthCard";

const API_BASE = "http://127.0.0.1:8000";

export default function Login({ role }) {
  const navigate = useNavigate();
  const { login, user, loading } = useAuth();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [loadingForm, setLoadingForm] = useState(false);

  // ✅ ROLE-AWARE redirect
  useEffect(() => {
    if (loading) return;

    if (user?.role === role) {
      navigate(role === "admin" ? "/admin" : "/dashboard");
    }
  }, [user, role, loading, navigate]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setLoadingForm(true);

    try {
      const loginRes = await axios.post(`${API_BASE}/auth/login`, null, {
        params: { email, password },
      });

      const token = loginRes.data.access_token;
      localStorage.setItem("token", token);

      const meRes = await axios.get(`${API_BASE}/auth/me`, {
        headers: { Authorization: `Bearer ${token}` },
      });

      login(meRes.data);
    } catch {
      setError("Invalid credentials");
    } finally {
      setLoadingForm(false);
    }
  };

  return (
    <AuthCard title={role === "admin" ? "Admin Login" : "User Login"}>
      <form onSubmit={handleSubmit} className="space-y-4">
        <input
          type="email"
          placeholder="Email"
          className="w-full p-2 border rounded"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />

        <input
          type="password"
          placeholder="Password"
          className="w-full p-2 border rounded"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />

        {error && <p className="text-red-500 text-sm">{error}</p>}

        <button
          type="submit"
          disabled={loadingForm}
          className="w-full bg-emerald-600 text-white py-2 rounded"
        >
          {loadingForm ? "Logging in..." : "Login"}
        </button>
      </form>

      <div className="text-center mt-4 text-sm">
        <span className="text-gray-600">Don’t have an account?</span>{" "}
        <button
          type="button"
          onClick={() =>
            navigate(role === "admin" ? "/admin/signup" : "/user/signup")
          }
          className="text-emerald-600 hover:underline font-medium"
        >
          Sign up
        </button>
      </div>
    </AuthCard>
  );
}
