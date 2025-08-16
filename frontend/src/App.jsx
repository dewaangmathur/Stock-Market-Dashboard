// frontend/src/App.jsx
import React, { useState, useEffect } from "react";
import Sidebar from "./components/Sidebar";
import ChartPanel from "./components/ChartPanel";
import IndicatorsPanel from "./components/IndicatorsPanel";
import PredictionPanel from "./components/PredictionPanel";
import { getCompanies } from "./api";
import "./styles.css";

export default function App() {
  const [selectedCompany, setSelectedCompany] = useState(null);

  useEffect(() => {
    async function fetchCompanies() {
      try {
        const companies = await getCompanies();
        if (companies.length > 0) {
          setSelectedCompany(companies[0]); // auto-select first company
        }
      } catch (err) {
        console.error("Error fetching companies:", err);
      }
    }
    fetchCompanies();
  }, []);

  return (
    <div className="dashboard">
      <div className="sidebar">
        <Sidebar onSelectCompany={setSelectedCompany} />
      </div>
      <div className="main">
        {selectedCompany ? (
          <>
            <ChartPanel company={selectedCompany} />
            <IndicatorsPanel company={selectedCompany} />
            <PredictionPanel company={selectedCompany} />
          </>
        ) : (
          <p>Loading companies...</p>
        )}
      </div>
    </div>
  );
}
