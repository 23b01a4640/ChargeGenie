import axios from "axios";

const API = "http://127.0.0.1:8000";

export const fetchRouteData = async (source, destination) => {
  const res = await axios.post(`${API}/maps/route`, {
    source,
    destination,
  });
  return res.data;
};
