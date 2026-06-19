import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def analyze_data(filename="sales.csv"):

    # ==========================
    # CREATE CHARTS FOLDER
    # ==========================

    os.makedirs("charts", exist_ok=True)

    # ==========================
    # LOAD DATA
    # ==========================

    df = pd.read_csv(f"dataset/{filename}")

    # ==========================
    # BASIC ANALYSIS
    # ==========================

    average_sales = df["Sales"].mean()
    total_sales = df["Sales"].sum()
    total_profit = df["Profit"].sum()

    highest_sales = df["Sales"].max()
    lowest_sales = df["Sales"].min()

    highest_month = df.loc[df["Sales"].idxmax(), "Month"]
    lowest_month = df.loc[df["Sales"].idxmin(), "Month"]

    # ==========================
    # PRINT DATA
    # ==========================

    print("\n========== DATA ==========\n")
    print(df)

    print("\n========== SUMMARY ==========\n")
    print(df.describe())

    # ==========================
    # BAR CHART
    # ==========================

    plt.figure(figsize=(8, 5))

    plt.bar(df["Month"], df["Sales"])

    plt.title("Monthly Sales")

    plt.xlabel("Month")

    plt.ylabel("Sales")

    plt.grid(axis="y", linestyle="--", alpha=0.4)

    plt.tight_layout()

    plt.savefig("charts/bar_chart.png")

    plt.close()

    # ==========================
    # SCATTER PLOT
    # ==========================

    plt.figure(figsize=(8, 5))

    plt.scatter(df["Sales"], df["Profit"], s=100)

    plt.title("Sales vs Profit")

    plt.xlabel("Sales")

    plt.ylabel("Profit")

    plt.grid(alpha=0.3)

    plt.tight_layout()

    plt.savefig("charts/scatter_plot.png")

    plt.close()

    # ==========================
    # HEATMAP
    # ==========================

    plt.figure(figsize=(6, 5))

    sns.heatmap(
        df.select_dtypes(include="number").corr(),
        annot=True,
        cmap="Blues",
        linewidths=1
    )

    plt.title("Correlation Heatmap")

    plt.tight_layout()

    plt.savefig("charts/heatmap.png")

    plt.close()

    # ==========================
    # AI INSIGHTS
    # ==========================

    insights = []

    insights.append(f"Dataset contains {len(df)} records.")

    missing = df.isnull().sum().sum()

    if missing == 0:
        insights.append("No missing values found.")
    else:
        insights.append(f"{missing} missing values detected.")

    insights.append(
        f"Highest sales were recorded in {highest_month}."
    )

    insights.append(
        f"Lowest sales were recorded in {lowest_month}."
    )

    if total_profit > 0:
        insights.append(
            "Business is running in overall profit."
        )
    else:
        insights.append(
            "Business is running at a loss."
        )

    correlation = df["Sales"].corr(df["Profit"])

    if correlation > 0.7:
        insights.append(
            "Sales and Profit have a strong positive correlation."
        )

    elif correlation > 0.3:
        insights.append(
            "Sales and Profit have a moderate correlation."
        )

    else:
        insights.append(
            "Sales and Profit have a weak correlation."
        )

    # ==========================
    # REPORT
    # ==========================

    report = f"""
========== DATA ANALYSIS REPORT ==========

Dataset Name       : {filename}

Average Sales      : {average_sales:.2f}

Total Sales        : {total_sales}

Total Profit       : {total_profit}

Highest Sales      : {highest_sales} ({highest_month})

Lowest Sales       : {lowest_sales} ({lowest_month})

========== AI INSIGHTS ==========
"""

    for item in insights:
        report += f"\n• {item}"

    report += """

========== CHARTS ==========
✔ Bar Chart
✔ Scatter Plot
✔ Heatmap

Charts saved successfully inside the 'charts' folder.
"""

    print(report)

    return report