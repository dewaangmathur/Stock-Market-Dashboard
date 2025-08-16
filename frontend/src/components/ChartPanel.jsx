// frontend/src/components/ChartPanel.jsx
import React, { useEffect, useState } from "react";
import { Line } from "react-chartjs-2";
import api from "../api";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
} from "chart.js";

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

export default function ChartPanel({ company }) {
  const [data, setData] = useState([]);

  useEffect(() => {
    if (company) {
      api.get(`/history/${company}`)
        .then(res => setData(res.data))
        .catch(err => console.error(err));
    }
  }, [company]);

  const chartData = {
    labels: data.map(d => d.Date),   // <-- uppercase D
    datasets: [
      {
        label: `${company} Stock Price`,
        data: data.map(d => d.Close),  // <-- uppercase C
        borderColor: "rgb(75, 192, 192)",
        backgroundColor: "rgba(75, 192, 192, 0.2)"
      }
    ]
  };

  return (
    <div className="chart-panel">
      <Line data={chartData} />
    </div>
  );
}
