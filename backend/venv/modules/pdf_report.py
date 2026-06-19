from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image,
)

from reportlab.lib.styles import getSampleStyleSheet

import os


def generate_pdf(report_text):

    os.makedirs("reports", exist_ok=True)

    pdf_file = "reports/analysis_report.pdf"

    doc = SimpleDocTemplate(pdf_file)

    styles = getSampleStyleSheet()

    story = []

    title = Paragraph(
        "<b><font size=18>NOVA AI DATA ANALYSIS REPORT</font></b>",
        styles["Title"],
    )

    story.append(title)

    story.append(Spacer(1, 20))

    # Report Text
    for line in report_text.split("\n"):

        if line.strip() == "":
            continue

        story.append(
            Paragraph(line, styles["BodyText"])
        )

    story.append(Spacer(1, 20))

    # Charts

    charts = [
        "charts/bar_chart.png",
        "charts/scatter_plot.png",
        "charts/heatmap.png",
    ]

    for chart in charts:

        if os.path.exists(chart):

            story.append(Spacer(1, 10))

            story.append(Image(chart, width=420, height=250))

    doc.build(story)

    return pdf_file