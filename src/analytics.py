from pathlib import Path
import csv
from config import HIGH_USAGE_THRESHOLD, LOW_USAGE_THRESHOLD
from src.billing import calculate_bill, calculate_due_date, get_days_late

def generate_analytics(filepath):
    
    # Convert relative path to absolute path based on project root
    file_path = Path(__file__).parent.parent / filepath
    
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
    
    # Initialize payment status counters
    paid_count = 0
    pending_count = 0
    paid_revenue = 0
    pending_revenue = 0
    
    # Initialize customer type counters
    residential_count = 0
    commercial_count = 0
    industrial_count = 0
    residential_revenue = 0
    commercial_revenue = 0
    industrial_revenue = 0
    
    # Initialize extreme usage and overdue counters
    extreme_usage_count = 0
    overdue_count = 0

    with open(str(file_path), "r", encoding="utf-8-sig") as file:

        reader = csv.DictReader(file)

        for row in reader:
            
            customer_id = row.get("customer_id", "").strip()
            name = row.get("customer_name", "").strip()
            billing_month = row.get("billing_month", "").strip()
            units = row.get("units_consumed", "").strip()
            payment_status = row.get("payment_status", "").strip()
            customer_type = row.get("customer_type", "").strip()

            # ignore missing data
            if not name or not units:
                continue

            # handle non-integer values
            try:
                units = int(units)
            except ValueError:
                continue

            # ignore negative values
            if units < 0:
                continue

            bill = calculate_bill(units)

            # Accumulate totals and track highest/lowest bills
            total_revenue += bill
            total_units += units
            total_customers += 1

            if bill > highest_bill:
                highest_bill = bill
                highest_customer = name

            if bill < lowest_bill:
                lowest_bill = bill
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
                paid_revenue += bill

            elif payment_status == "Pending":
                pending_count += 1
                pending_revenue += bill

            # Categorize customer type
            if customer_type == "Residential":
                residential_count += 1
                residential_revenue += bill
            elif customer_type == "Commercial":
                commercial_count += 1
                commercial_revenue += bill
            elif customer_type == "Industrial":
                industrial_count += 1
                industrial_revenue += bill

            
            
            # Getting due date and calculating overdue customers
            due_date = calculate_due_date(billing_month)

            days_late = get_days_late(due_date)

            if days_late > 0 and payment_status == "Pending":
                overdue_count += 1

            if units > 1000 and customer_type == "Industrial":
                extreme_usage_count += 1
            elif units > 500 and customer_type == "Commercial":
                extreme_usage_count += 1
            elif units > 300 and customer_type == "Residential":
                extreme_usage_count += 1

    average_consumption = total_units / total_customers if total_customers > 0 else 0
    average_bill = total_revenue / total_customers if total_customers > 0 else 0

    # insight based on usage
    if high_usage > low_usage and high_usage > mid_usage:
     insight1 = "Majority customers are high usage consumers."
    elif low_usage > high_usage and low_usage > mid_usage:
     insight1 = "Majority customers are low usage consumers."
    else:
     insight1 = "Majority customers are medium usage consumers."

    # insight based on payment status
    if pending_count > paid_count:
        insight2 = "Most customers have pending payments."
    else:
        insight2 = "Most customers have completed payments."

    # insight based on customer type revenue
    revenue_map = {
        "Residential": residential_revenue,
        "Commercial": commercial_revenue,
        "Industrial": industrial_revenue
    }

    top_revenue_type = max(revenue_map, key=revenue_map.get)

    insight3 = f"{top_revenue_type} customers generate the highest revenue."

    # overdue customers insight
    if overdue_count > 0:
        insight4 = f"There are {overdue_count} overdue customers who may require follow-up."
    else:
        insight4 = "No overdue customers at the moment."

    return {
        "total_revenue": total_revenue,
        "highest_bill": highest_bill,
        "highest_customer": highest_customer,
        "lowest_bill": lowest_bill,
        "lowest_customer": lowest_customer,
        "average_consumption": average_consumption,
        "average_bill": average_bill,
        "high_usage": high_usage,
        "medium_usage": mid_usage,
        "low_usage": low_usage,
        "total_customers": total_customers,
        "overdue_count": overdue_count,
        "extreme_usage_count": extreme_usage_count,
        "paid_count": paid_count,
        "pending_count": pending_count,
        "paid_revenue": paid_revenue,
        "pending_revenue": pending_revenue,
        "residential_count": residential_count,
        "commercial_count": commercial_count,
        "industrial_count": industrial_count,
        "residential_revenue": residential_revenue,
        "commercial_revenue": commercial_revenue,
        "industrial_revenue": industrial_revenue,
        "extreme_usage_count": extreme_usage_count,
        "insight1": insight1,
        "insight2": insight2,
        "insight3": insight3,
        "insight4": insight4
    }
