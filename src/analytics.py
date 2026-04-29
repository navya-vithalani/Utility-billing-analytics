import csv
from config import HIGH_USAGE_THRESHOLD, LOW_USAGE_THRESHOLD
from src.billing import calculate_bill



def generate_analytics(filepath):

    total_revenue = 0
    total_units = 0
    highest_bill = 0
    highest_customer = ""
    lowest_bill = float('inf')
    lowest_customer = ""
    high_usage = 0
    low_usage = 0
    mid_usage = 0
    count = 0

    with open(filepath, "r", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row in reader:

            name = row.get("Customer Name", "").strip()
            units_str = row.get("Units Consumed", "").strip()

            # ignore missing data
            if not name or not units_str:
                continue

            # handle non-integer values
            try:
                units = int(units_str)
            except ValueError:
                continue

            # ignore negative values
            if units < 0:
                continue

            bill = calculate_bill(units)

            # Accumulate totals and track highest/lowest bills
            total_revenue += bill
            total_units += units
            count += 1

            if bill > highest_bill:
                highest_bill = bill
                highest_customer = name

            if bill < lowest_bill:
                lowest_bill = bill
                lowest_customer = name

            # Categorize usage for insights
            if units > HIGH_USAGE_THRESHOLD:
                high_usage += 1
            elif units < LOW_USAGE_THRESHOLD:
                low_usage += 1
            else:
                mid_usage += 1

    average_consumption = total_units / count if count > 0 else 0
    average_bill = total_revenue / count if count > 0 else 0

    if high_usage > low_usage and high_usage > mid_usage:
     insight1 = "Majority customers are high usage consumers."
    elif low_usage > high_usage and low_usage > mid_usage:
     insight1 = "Majority customers are low usage consumers."
    else:
     insight1 = "Majority customers are medium usage consumers."

    return {
        "total_revenue": total_revenue,
        "highest_bill": highest_bill,
        "highest_customer": highest_customer,
        "lowest_bill": lowest_bill,
        "lowest_customer": lowest_customer,
        "average_consumption": average_consumption,
        "insight1": insight1,
        "average_bill": average_bill,
        "high_usage": high_usage,
        "medium_usage": mid_usage,
        "low_usage": low_usage
    }