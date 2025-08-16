// frontend/src/components/PredictionPanel.jsx
import React, { useEffect, useState } from "react";
import api from "../api";

export default function PredictionPanel({ company }) {
  const [prediction, setPrediction] = useState(null);

  useEffect(() => {
    if (company) {
      api.get(`/predict/${company}`)
        .then(res => setPrediction(res.data))
        .catch(err => console.error(err));
    }
  }, [company]);

  if (!prediction) return null;

  return (
    <div className="prediction-panel">
      <h3>AI Forecast</h3>
      <p>Next Day Price: {prediction.predicted_close}</p>
    </div>
  );
}
