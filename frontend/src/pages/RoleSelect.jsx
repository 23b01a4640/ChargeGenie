import { useNavigate } from "react-router-dom";

export default function RoleSelect() {
  const navigate = useNavigate();

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50">
      <div className="bg-white p-10 rounded-2xl shadow-xl max-w-lg w-full text-center">
        <h1 className="text-3xl font-semibold text-gray-800 mb-4">
          Welcome to ChargeGenie
        </h1>

        <p className="text-gray-500 mb-8">
          Choose how you want to continue
        </p>

        <div className="space-y-4">
          <button
            onClick={() => navigate("/user/login")}
            className="w-full py-3 rounded-xl border border-emerald-600 text-emerald-600 font-medium hover:bg-emerald-50 transition"
          >
            I’m an EV User
          </button>

          <button
            onClick={() => navigate("/admin/login")}
            className="w-full py-3 rounded-xl bg-emerald-600 text-white font-medium hover:bg-emerald-700 transition"
          >
            I’m a Station Admin
          </button>
        </div>
      </div>
    </div>
  );
}
