import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
from datetime import datetime


def create_visualizations(data):
    """Generate visualization charts from analytics data."""
    # Create reports folder if it doesn't exist
    reports_path = Path("static/charts")
    reports_path.mkdir(exist_ok=True)

    # =========================================================
    # 1. CUSTOMER TYPE DISTRIBUTION (PIE CHART)
    # =========================================================
    customer_labels = ["Residential", "Commercial", "Industrial"]

    customer_counts = [
        data["residential_count"],
        data["commercial_count"],
        data["industrial_count"]
    ]

    explode = [0.03, 0.03, 0.03]

    plt.figure(figsize=(7, 7))
    plt.pie(
        customer_counts,
        labels=customer_labels,
        autopct="%1.1f%%",
        explode=explode
    )
    plt.title("Customer Type Distribution")
    plt.tight_layout()
    plt.savefig(reports_path / f"customer_distribution.png")
    plt.close()

    # =========================================================
    # 2. REVENUE BY CUSTOMER TYPE
    # =========================================================
    revenues = [
        data["residential_revenue"],
        data["commercial_revenue"],
        data["industrial_revenue"]
    ]

    plt.figure(figsize=(8, 5))
    bars = plt.bar(customer_labels, revenues)

    # Add value labels
    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f"₹{height:.0f}",
            ha='center',
            va='bottom'
        )

    plt.title("Revenue by Customer Type")
    plt.xlabel("Customer Type")
    plt.ylabel("Revenue (₹)")
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig(reports_path / f"revenue_by_type.png")
    plt.close()

    # =========================================================
    # 3. PAYMENT STATUS OVERVIEW
    # =========================================================
    payment_labels = ["Paid", "Pending"]

    payment_counts = [
        data["paid_count"],
        data["pending_count"]
    ]

    plt.figure(figsize=(7, 5))
    bars = plt.bar(payment_labels, payment_counts)

    # Add labels
    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f"{height}",
            ha='center',
            va='bottom'
        )

    plt.title("Payment Status Overview")
    plt.xlabel("Payment Status")
    plt.ylabel("Customer Count")
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig(reports_path / f"payment_status.png")
    plt.close()

    # =========================================================
    # 4. USAGE CATEGORY DISTRIBUTION
    # =========================================================
    usage_labels = [
        "Low Usage",
        "Medium Usage",
        "High Usage"
    ]

    usage_counts = [
        data["low_usage"],
        data["medium_usage"],
        data["high_usage"]
    ]

    plt.figure(figsize=(8, 5))
    bars = plt.bar(usage_labels, usage_counts)

    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f"{height}",
            ha='center',
            va='bottom'
        )

    plt.title("Electricity Usage Categories")
    plt.xlabel("Usage Category")
    plt.ylabel("Customer Count")
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig(reports_path / f"usage_distribution.png")
    plt.close()

    # =========================================================
    # 5. PAID VS PENDING REVENUE
    # =========================================================
    revenue_labels = ["Paid Revenue", "Pending Revenue"]

    revenue_values = [
        data["paid_revenue"],
        data["pending_revenue"]
    ]

    plt.figure(figsize=(8, 5))
    bars = plt.bar(revenue_labels, revenue_values)

    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f"₹{height:.0f}",
            ha='center',
            va='bottom'
        )

    plt.title("Paid vs Pending Revenue")
    plt.ylabel("Revenue (₹)")
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig(reports_path / f"paid_vs_pending_revenue.png")
    plt.close()

    # =========================================================
    # 6. TAX, DISCOUNT, PENALTY COMPARISON
    # =========================================================
    finance_labels = [
        "Tax",
        "Discount",
        "Penalty"
    ]

    finance_values = [
        data["total_tax_collected"],
        data["total_discounts_given"],
        data["total_penalties_collected"]
    ]

    plt.figure(figsize=(8, 5))
    bars = plt.bar(finance_labels, finance_values)

    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f"₹{height:.0f}",
            ha='center',
            va='bottom'
        )

    plt.title("Tax, Discount, and Penalty Overview")
    plt.ylabel("Amount (₹)")
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig(reports_path / f"finance_overview.png")
    plt.close()

    # =========================================================
    # 7. CUSTOMER CATEGORY REVENUE SHARE
    # =========================================================
    plt.figure(figsize=(7, 7))
    plt.pie(
        revenues,
        labels=customer_labels,
        autopct="%1.1f%%",
        explode=explode
    )
    plt.title("Revenue Share by Customer Type")
    plt.tight_layout()
    plt.savefig(reports_path / f"revenue_share.png")
    plt.close()

    # =========================================================
    # 8. UNITS CONSUMED VS TOTAL BILL
    # =========================================================
    plt.figure(figsize=(8, 5))
    plt.scatter(
        data["all_units"],
        data["all_bills"]
    )
    plt.title("Units Consumed vs Total Bill")
    plt.xlabel("Units Consumed (kWh)")
    plt.ylabel("Total Bill (₹)")
    plt.grid(alpha=0.5)
    plt.tight_layout()
    plt.savefig(reports_path / f"units_vs_bill.png")
    plt.close()

    # =========================================================
    # 9. TOP 5 HIGHEST PAYING CUSTOMERS
    # =========================================================
    top_customers = data["top_5_customers"]

    customer_names = [
        customer["name"]
        for customer in top_customers
    ]

    customer_bills = [
        customer["total_bill"]
        for customer in top_customers
    ]

    plt.figure(figsize=(10, 5))
    bars = plt.bar(customer_names, customer_bills)

    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f"₹{height:.0f}",
            ha='center',
            va='bottom'
        )

    plt.title("Top 5 Highest Paying Customers")
    plt.xlabel("Customer")
    plt.ylabel("Total Bill (₹)")
    plt.xticks(rotation=10)
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig(reports_path / f"top_5_customers.png")
    plt.close()

    # =========================================================
    # FINAL MESSAGE
    # =========================================================
    print("\nVisualizations generated successfully.")
    print(f"Reports saved in: {reports_path.resolve()}")