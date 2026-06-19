import "./ChartGallery.css";

const BASE_URL = "http://127.0.0.1:8000";

export default function ChartGallery({ charts }) {

  if (!charts) {
    return (
      <div className="chart-gallery">
        <h2>📈 Charts</h2>
        <p>Run analysis to generate charts.</p>
      </div>
    );
  }

  return (
    <div className="chart-gallery">

      <h2>📈 Generated Charts</h2>

      <div className="charts">

        {charts.map((chart, index) => (

          <img
            key={index}
            src={BASE_URL + chart}
            alt={`Chart ${index}`}
          />

        ))}

      </div>

    </div>
  );
}