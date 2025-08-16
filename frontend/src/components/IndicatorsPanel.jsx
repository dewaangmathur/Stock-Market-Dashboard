// frontend/src/components/IndicatorsPanel.jsx
import React, { useEffect, useState } from "react";
import api from "../api";

export default function IndicatorsPanel({ company }) {
  const [indicators, setIndicators] = useState(null);

  useEffect(() => {
    if (company) {
      api.get(`/indicators/${company}`)
        .then(res => setIndicators(res.data))
        .catch(err => console.error(err));
    }
  }, [company]);

  if (!indicators) return null;

  const formatValue = (value) => {
    if (value === null || value === undefined || Number.isNaN(value)) {
      return "N/A";
    }
    return value;
  };

  return (
    <div className="indicators-panel">
      <h3>Technical Indicators</h3>
      <ul>
        <li>52-Week High: {formatValue(indicators.high_52w)}</li>
        <li>52-Week Low: {formatValue(indicators.low_52w)}</li>
        <li>SMA(50): {formatValue(indicators.sma_50)}</li>
        <li>RSI: {formatValue(indicators.rsi)}</li>
        <li>Average Volume: {formatValue(indicators.avg_volume)}</li>
      </ul>
    </div>
  );
}
