// frontend/src/hooks/useStockData.js
import { useState, useEffect } from "react";
import api from "../api";

export default function useStockData(company) {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (!company) return;

    const fetchData = async () => {
      setLoading(true);
      setError(null);
      try {
        const res = await api.get(`/stock/${company}`);
        setData(res.data);
      } catch (err) {
        setError("Failed to fetch stock data.");
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [company]);

  return { data, loading, error };
}
