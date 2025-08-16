// frontend/src/components/Sidebar.jsx
import React, { useEffect, useState } from "react";
import api from "../api";

export default function Sidebar({ onSelectCompany }) {
  const [companies, setCompanies] = useState([]);

  useEffect(() => {
    api.get("/companies")
      .then(res => setCompanies(res.data))
      .catch(err => console.error("Error fetching companies:", err));
  }, []);

  return (
    <div className="sidebar-list">
      {companies.map((symbol) => (
        <div
          key={symbol}
          className="sidebar-item"
          onClick={() => onSelectCompany(symbol)}
        >
          {symbol}
        </div>
      ))}
    </div>
  );
}
