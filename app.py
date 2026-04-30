from flask import Flask, render_template, request, redirect
import csv

from src.analytics import generate_analytics
from src.visualisations import create_visualizations
from src.billing import (
    calculate_total_bill,
    get_days_late,
    calculate_due_date,
    calculate_bill
)
import config

app = Flask(__name__)


# =========================
# LANDING PAGE
# =========================
@app.route("/")
def home_page():
    return render_template(
        "index.html"
    )


@app.route("/generate-bill", methods=["POST"])
def generate_bill_page():
    data = request.form

    units = int(data["units"])
    billing_month = data["billing_month"]

    bill = calculate_total_bill(units, get_days_late(calculate_due_date(billing_month)))
    details = calculate_bill(units)

    # Extract bill components
    total_bill = bill["total_bill"]
    discount = details["discount"]
    tax = details["tax"]
    due_date = bill["due_date"]
    energy_charge = details["energy_charge"]
    fixed_charge = config.FIXED_CHARGE
    penalty = bill["penalty"]
    days_late = bill["days_late"]

    return render_template(
        "index.html",
        discount=discount,
        tax=tax,
        bill=total_bill,
        due_date=due_date,
        energy_charge=energy_charge,
        fixed_charge=fixed_charge,
        penalty=penalty,
        days_late=days_late
    )


@app.route("/view")
def view_page():
    customers = []

    # Read customer data from CSV
    with open(
        "data/customers.csv",
        "r",
        encoding="utf-8-sig"
    ) as file:
        reader = csv.DictReader(file)
        for row in reader:
            customers.append(row)

    # Search by customer name or ID
    search = request.args.get("search", "").lower()
    if search:
        customers = [
            customer for customer in customers
            if (
                search in customer["customer_name"].lower()
                or search in customer["customer_id"].lower()
            )
        ]

    # Filter by customer type
    customer_type = request.args.get("type", "")
    if customer_type:
        customers = [
            customer for customer in customers
            if customer["customer_type"] == customer_type
        ]

    # Sort customers
    sort = request.args.get("sort", "")
    if sort == "units":
        customers.sort(
            key=lambda x: int(x["units_consumed"]),
            reverse=True
        )
    elif sort == "name":
        customers.sort(
            key=lambda x: x["customer_name"]
        )

    # Toggle for showing inactive customers
    show_inactive = request.args.get("show_inactive") is not None
    if not show_inactive:
        customers = [
            customer for customer in customers
            if customer.get("status", "Active") == "Active"
        ]   

    return render_template(
        "view.html",
        customers=customers,
        show_inactive=show_inactive
    )

# =========================
# ANALYZE PAGE
# =========================
@app.route("/analyze")
def analyze_page():
    analytics = generate_analytics("data/customers.csv")

    # Generate visualization charts
    create_visualizations(analytics)

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

    # Read customer data from CSV
    with open(
        "data/customers.csv",
        "r",
        encoding="utf-8-sig"
    ) as file:
        reader = csv.DictReader(file)
        for row in reader:
            customers.append(row)

    # Search by customer name or ID
    search = request.args.get("search", "").lower()
    if search:
        customers = [
            customer for customer in customers
            if (
                search in customer["customer_name"].lower()
                or search in customer["customer_id"].lower()
            )
        ]

    return render_template(
        "modify.html",
        customers=customers
    )


@app.route(
    "/add",
    methods=["GET", "POST"]
)
def add_customer():
    # Generate next customer ID based on existing IDs
    customer_ids = []

    with open(
        "data/customers.csv",
        "r",
        encoding="utf-8-sig"
    ) as file:
        reader = csv.DictReader(file)
        for row in reader:
            customer_ids.append(int(row["customer_id"]))

    new_customer_id = str(max(customer_ids) + 1)

    if request.method == "POST":
        new_customer = {
            "customer_id": new_customer_id,
            "customer_name": request.form["customer_name"],
            "billing_month": request.form["billing_month"],
            "units_consumed": request.form["units_consumed"],
            "payment_status": request.form["payment_status"],
            "customer_type": request.form["customer_type"]
        }

        # Append new customer to CSV
        with open(
            "data/customers.csv",
            "a",
            newline="",
            encoding="utf-8-sig"
        ) as file:
            fieldnames = [
                "customer_id",
                "customer_name",
                "billing_month",
                "units_consumed",
                "payment_status",
                "customer_type"
            ]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(new_customer)

        return redirect("/modify")

    return render_template(
        "add_customer.html",
        new_customer_id=new_customer_id
    )


@app.route(
    "/edit/<customer_id>",
    methods=["GET", "POST"]
)
def edit_customer(customer_id):
    customers = []
    customer_to_edit = None

    # Read all customer data
    with open(
        "data/customers.csv",
        "r",
        encoding="utf-8-sig"
    ) as file:
        reader = csv.DictReader(file)
        for row in reader:
            customers.append(row)
            if row["customer_id"] == customer_id:
                customer_to_edit = row

    # Update customer information on POST request
    if request.method == "POST":
        updated_customers = []

        for customer in customers:
            if customer["customer_id"] == customer_id:
                customer["customer_name"] = request.form["customer_name"]
                customer["customer_type"] = request.form["customer_type"]
                customer["units_consumed"] = request.form["units_consumed"]
                customer["billing_month"] = request.form["billing_month"]
                customer["payment_status"] = request.form["payment_status"]

            updated_customers.append(customer)

        # Save updated data to CSV
        with open(
            "data/customers.csv",
            "w",
            newline="",
            encoding="utf-8-sig"
        ) as file:
            fieldnames = updated_customers[0].keys()
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(updated_customers)

        return redirect("/modify")

    return render_template(
        "edit_customer.html",
        customer=customer_to_edit
    )


@app.route("/deactivate/<customer_id>")
def deactivate_customer(customer_id):
    updated_rows = []

    # Read and filter out the customer to be deactivated
    with open(
        "data/customers.csv",
        "r",
        encoding="utf-8-sig"
    ) as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["customer_id"] == customer_id:
                row["status"] = "Inactive"
            updated_rows.append(row)

    # Write remaining customers back to CSV
    with open(
        "data/customers.csv",
        "w",
        newline="",
        encoding="utf-8-sig"
    ) as file:
        fieldnames = updated_rows[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(updated_rows)

    return redirect("/modify")


@app.route("/activate/<customer_id>")
def activate_customer(customer_id):
    updated_rows = []

    # Read and filter out the customer to be activated
    with open(
        "data/customers.csv",
        "r",
        encoding="utf-8-sig"
    ) as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["customer_id"] == customer_id:
                row["status"] = "Active"
            updated_rows.append(row)

    # Write remaining customers back to CSV
    with open(
        "data/customers.csv",
        "w",
        newline="",
        encoding="utf-8-sig"
    ) as file:
        fieldnames = updated_rows[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(updated_rows)

    return redirect("/modify")

if __name__ == "__main__":
    app.run(debug=True)