// frontend/src/api.js
import axios from "axios";

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || "http://localhost:8000",
});

// Named exports for API calls
export async function getCompanies() {
  const res = await api.get("/companies");
  return res.data;
}

export async function getStock(symbol) {
  const res = await api.get(`/stock/${symbol}`);
  return res.data;
}

export async function getIndicators(symbol) {
  const res = await api.get(`/indicators/${symbol}`);
  return res.data;
}

export async function getPrediction(symbol) {
  const res = await api.get(`/predict/${symbol}`);
  return res.data;
}

export default api;
