import "./PDFCard.css";

const BASE_URL = "http://127.0.0.1:8000";

export default function PDFCard({ pdf }) {

  return (

    <div className="pdf-card">

      <h2>📄 PDF Report</h2>

      {pdf ? (

        <a
          href={BASE_URL + pdf}
          target="_blank"
          rel="noreferrer"
        >

          <button>

            Download Report

          </button>

        </a>

      ) : (

        <p>No report generated yet.</p>

      )}

    </div>

  );

}