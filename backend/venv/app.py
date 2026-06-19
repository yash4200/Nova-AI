from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from modules.ai import ask_ai
from modules.data_analysis import analyze_data
from modules.pdf_report import generate_pdf

from pydantic import BaseModel

app = FastAPI()

# ----------------------------
# CORS
# ----------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------------------
# Static Files
# ----------------------------

app.mount("/charts", StaticFiles(directory="charts"), name="charts")

app.mount("/reports", StaticFiles(directory="reports"), name="reports")

# ----------------------------
# Request Model
# ----------------------------

class Prompt(BaseModel):
    text: str


# ----------------------------
# Home
# ----------------------------

@app.get("/")
def home():

    return {
        "status":"Nova Running"
    }


# ----------------------------
# Ask AI
# ----------------------------

@app.post("/ask")
def ask(prompt: Prompt):

    answer = ask_ai(prompt.text)

    return {

        "response":answer

    }


# ----------------------------
# Analyze
# ----------------------------

@app.post("/analyze")
def analyze():

    report = analyze_data("sales.csv")

    generate_pdf(report)

    return {

        "message":"Analysis Complete",

        "report":report,

        "charts":[

            "/charts/bar_chart.png",

            "/charts/scatter_plot.png",

            "/charts/heatmap.png"

        ],

        "pdf":"/reports/analysis_report.pdf"

    }