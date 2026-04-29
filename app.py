from flask import Flask, render_template
import csv
from src.analytics import generate_analytics

app = Flask(__name__)


# =========================
# VIEW PAGE
# =========================
@app.route("/")
def home_page():
    return render_template(
        "index.html"
    )

@app.route("/view")
def view_page():

    customers = []

    with open(
        "data/customers.csv",
        "r",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:
            customers.append(row)

    return render_template(
        "view.html",
        customers=customers
    )


# =========================
# ANALYZE PAGE
# =========================
@app.route("/analyze")
def analyze_page():

    analytics = generate_analytics(
        "data/customers.csv"
    )

    return render_template(
        "analyze.html",
        analytics=analytics
    )


# =========================
# MODIFY PAGE
# =========================
@app.route("/modify")
def modify_page():

    customers = []

    with open(
        "data/customers.csv",
        "r",
        encoding="utf-8-sig"
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:
            customers.append(row)

    return render_template(
        "modify.html",
        customers=customers
    )


if __name__ == "__main__":
    app.run(debug=True)