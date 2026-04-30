from pathlib import Path
import sys
import csv

# Add parent and current directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent))

from config import HIGH_USAGE_THRESHOLD, LOW_USAGE_THRESHOLD
from billing import calculate_total_bill, calculate_due_date, get_days_late


def generate_analytics(filepath):
    """Generate analytics from customer billing data."""
    # Convert relative path to absolute path based on project root
    file_path = Path(__file__).parent.parent / filepath

    # =========================================================
    # INITIALIZE COUNTERS AND ACCUMULATORS
    # =========================================================
    total_revenue = 0
    total_units = 0
    highest_bill = 0
    highest_customer = ""
    lowest_bill = float('inf')
    lowest_customer = ""
    high_usage = 0
    low_usage = 0
    mid_usage = 0
    total_customers = 0
    skipped_rows = 0
    all_units = []
    all_bills = []
    customer_bill_data = []

    # Payment status counters
    paid_count = 0
    pending_count = 0
    paid_revenue = 0
    pending_revenue = 0

    # Customer type counters
    residential_count = 0
    commercial_count = 0
    industrial_count = 0
    residential_revenue = 0
    commercial_revenue = 0
    industrial_revenue = 0

    # Extreme usage and overdue counters
    extreme_usage_count = 0
    overdue_count = 0

    # Tax, discount, and penalty accumulators
    total_tax_collected = 0
    total_discounts_given = 0
    total_penalties_collected = 0

    # =========================================================
    # READ AND PROCESS CUSTOMER DATA
    # =========================================================
    with open(str(file_path), "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        for row in reader:
            # Extract customer data
            customer_id = row.get("customer_id", "").strip()
            name = row.get("customer_name", "").strip()
            billing_month = row.get("billing_month", "").strip()
            units = row.get("units_consumed", "").strip()
            payment_status = row.get("payment_status", "").strip()
            customer_type = row.get("customer_type", "").strip()

            # Skip rows with missing data
            if not name or not units:
                skipped_rows += 1
                continue

            # Handle non-integer values
            try:
                units = int(units)
            except ValueError:
                skipped_rows += 1
                continue

            # Skip negative values
            if units < 0:
                skipped_rows += 1
                continue

            # Calculate billing information
            due_date = calculate_due_date(billing_month)
            days_late = get_days_late(due_date)
            bill = calculate_total_bill(units, days_late)

            bill_details = bill["bill_details"]
            base_bill = bill_details["bill_amount"]
            tax = bill_details["tax"]
            discount = bill_details["discount"]
            penalty = bill["penalty"]

            status = bill["status"]
            total_bill = bill["total_bill"]

            # Accumulate units and bills
            all_units.append(units)
            all_bills.append(total_bill)
            customer_bill_data.append(
                {"name": name, "units": units, "total_bill": total_bill}
            )

            # Accumulate totals and track highest/lowest bills
            total_revenue += total_bill
            total_units += units
            total_customers += 1

            if total_bill > highest_bill:
                highest_bill = total_bill
                highest_customer = name

            if total_bill < lowest_bill:
                lowest_bill = total_bill
                lowest_customer = name

            # Categorize usage
            if units > HIGH_USAGE_THRESHOLD:
                high_usage += 1
            elif units < LOW_USAGE_THRESHOLD:
                low_usage += 1
            else:
                mid_usage += 1

            # Categorize payment status
            if payment_status == "Paid":
                paid_count += 1
                paid_revenue += total_bill
            elif payment_status == "Pending":
                pending_count += 1
                pending_revenue += total_bill

            # Categorize customer type
            if customer_type == "Residential":
                residential_count += 1
                residential_revenue += total_bill
            elif customer_type == "Commercial":
                commercial_count += 1
                commercial_revenue += total_bill
            elif customer_type == "Industrial":
                industrial_count += 1
                industrial_revenue += total_bill

            # Track overdue customers
            if days_late > 0 and payment_status == "Pending":
                overdue_count += 1

            # Track extreme usage customers
            if units > 1000 and customer_type == "Industrial":
                extreme_usage_count += 1
            elif units > 500 and customer_type == "Commercial":
                extreme_usage_count += 1
            elif units > 300 and customer_type == "Residential":
                extreme_usage_count += 1

            # Accumulate tax, discount, and penalty totals
            total_tax_collected += tax
            total_discounts_given += discount
            total_penalties_collected += penalty

    # =========================================================
    # CALCULATE ANALYTICS METRICS
    # =========================================================
    # Calculate collection rate
    collection_rate = (
        (paid_revenue / total_revenue) * 100
        if total_revenue > 0
        else 0
    )

    # Get top 5 customers
    top_5_customers = sorted(
        customer_bill_data,
        key=lambda customer: customer["total_bill"],
        reverse=True
    )[:5]

    average_consumption = (
        total_units / total_customers if total_customers > 0 else 0
    )
    average_bill = total_revenue / total_customers if total_customers > 0 else 0

    # =========================================================
    # GENERATE INSIGHTS
    # =========================================================
    # Insight: Usage pattern
    if high_usage > low_usage and high_usage > mid_usage:
        insight1 = "Majority customers are high usage consumers."
    elif low_usage > high_usage and low_usage > mid_usage:
        insight1 = "Majority customers are low usage consumers."
    else:
        insight1 = "Majority customers are medium usage consumers."

    # Insight: Payment status
    if pending_count > paid_count:
        insight2 = "Most customers have pending payments."
    else:
        insight2 = "Most customers have completed payments."

    # Insight: Customer type revenue
    revenue_map = {
        "Residential": residential_revenue,
        "Commercial": commercial_revenue,
        "Industrial": industrial_revenue
    }
    top_revenue_type = max(revenue_map, key=revenue_map.get)
    insight3 = f"{top_revenue_type} customers generate the highest revenue."

    # Insight: Overdue customers
    if overdue_count > 0:
        insight4 = f"There are {overdue_count} overdue customers who may require follow-up."
    else:
        insight4 = "No overdue customers at the moment."

    # Insight: Discount vs Penalty
    if total_discounts_given > total_penalties_collected:
        insight5 = "The company is giving more discounts than it is collecting in penalties."
    elif total_penalties_collected > total_discounts_given:
        insight5 = "The company is collecting more in penalties than it is giving in discounts."
    else:
        insight5 = "The total discounts given and penalties collected are equal."

    # Insight: Tax collected
    if total_tax_collected > 0:
        insight6 = f"The company has collected a total of ₹{total_tax_collected:.2f} in taxes."
    else:
        insight6 = "No taxes have been collected."

    # Insight: Invalid data
    if skipped_rows > 0:
        insight7 = f"Skipped {skipped_rows} rows due to invalid or missing data."
    else:
        insight7 = "No rows were skipped due to data issues."

    # Insight: Collection rate
    if collection_rate > 80:
        insight8 = f"The collection rate is strong at {collection_rate:.2f}%."
    elif collection_rate > 50:
        insight8 = f"The collection rate is moderate at {collection_rate:.2f}%."
    else:
        insight8 = f"The collection rate is weak at {collection_rate:.2f}%."

    # =========================================================
    # RETURN ANALYTICS DICTIONARY
    # =========================================================
    return {
        "total_revenue": round(total_revenue, 2),
        "highest_bill": round(highest_bill, 2),
        "highest_customer": highest_customer,
        "lowest_bill": round(lowest_bill, 2),
        "lowest_customer": lowest_customer,
        "average_consumption": round(average_consumption, 2),
        "average_bill": round(average_bill, 2),
        "high_usage": high_usage,
        "medium_usage": mid_usage,
        "low_usage": low_usage,
        "total_customers": total_customers,
        "overdue_count": overdue_count,
        "extreme_usage_count": extreme_usage_count,
        "paid_count": paid_count,
        "pending_count": pending_count,
        "paid_revenue": round(paid_revenue, 2),
        "pending_revenue": round(pending_revenue, 2),
        "residential_count": residential_count,
        "commercial_count": commercial_count,
        "industrial_count": industrial_count,
        "residential_revenue": round(residential_revenue, 2),
        "commercial_revenue": round(commercial_revenue, 2),
        "industrial_revenue": round(industrial_revenue, 2),
        "total_tax_collected": round(total_tax_collected, 2),
        "total_discounts_given": round(total_discounts_given, 2),
        "total_penalties_collected": round(total_penalties_collected, 2),
        "top_5_customers": top_5_customers,
        "all_units": all_units,
        "all_bills": all_bills,
        "bill": customer_bill_data,
        "insight1": insight1,
        "insight2": insight2,
        "insight3": insight3,
        "insight4": insight4,
        "insight5": insight5,
        "insight6": insight6,
        "insight7": insight7,
        "insight8": insight8
    }
