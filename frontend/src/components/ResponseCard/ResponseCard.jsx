import "./ResponseCard.css";

export default function ResponseCard({ report }) {

    return (

        <div className="response-card">

            <h2>📄 Analysis Report</h2>

            <pre>

                {report || "Run analysis to see report."}

            </pre>

        </div>

    );

}