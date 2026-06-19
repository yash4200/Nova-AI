import "./AnalysisCard.css";
import { useState } from "react";
import api from "../../services/api";

export default function AnalysisCard({ setAnalysisData }) {
  const [loading, setLoading] = useState(false);

  const analyze = async () => {
    try {
      setLoading(true);

      const res = await api.post("/analyze");
      setAnalysisData(res.data);
      alert("Analysis Completed!");

    } catch (err) {
      console.log(err);

      alert("Analysis Failed");
    }

    setLoading(false);
  };

  return (
    <div className="analysis-card">

      <h2>📊 Data Analysis</h2>

      <p>
        Analyze your dataset and generate charts + PDF report.
      </p>

      <button onClick={analyze} disabled={loading}>
        {loading ? "Analyzing..." : "Analyze Dataset"}
      </button>

    </div>
  );
}