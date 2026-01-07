const API = "http://127.0.0.1:8000";

export async function getVehicleProfile() {
  const res = await fetch(`${API}/vehicle/me`, {
    headers: {
      Authorization: `Bearer ${localStorage.getItem("token")}`,
    },
  });

  return res.json();
}

export async function saveVehicleProfile(payload) {
  const res = await fetch(`${API}/vehicle/me`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${localStorage.getItem("token")}`,
    },
    body: JSON.stringify(payload),
  });

  if (!res.ok) {
    throw new Error("Failed to save vehicle profile");
  }

  return res.json();
}
