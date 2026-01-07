import { BrowserRouter, Routes, Route } from "react-router-dom";

import Login from "./pages/Login";
import Signup from "./pages/Signup";
import Dashboard from "./pages/Dashboard";
import AdminDashboard from "./pages/AdminDashboard";
import RoleSelect from "./pages/RoleSelect";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<RoleSelect />} />

        <Route path="/user/login" element={<Login role="user" />} />
        <Route path="/user/signup" element={<Signup role="user" />} />

        <Route path="/admin/login" element={<Login role="admin" />} />
        <Route path="/admin/signup" element={<Signup role="admin" />} />

        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/admin" element={<AdminDashboard />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
