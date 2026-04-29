import csv
from src.billing import calculate_bill
from src.utils import format_currency, separator
from src.analytics import generate_analytics


print("Reading customer data and calculating bills...\n")


try:

    print(f"{'Customer':^20}| {'Units(kWh)':^10} | {'Bill':^12}")
    separator(50, "-")

    with open("data/customers.csv", mode="r", newline="", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row in reader:

            name = row.get("Customer Name", "").strip()
            units_str = row.get("Units Consumed", "").strip()


            # Missing data check
            if not name or not units_str:

                print("Skipping invalid row: missing customer name or units.")
                print("." * 50)

                continue


            # Integer conversion check
            try:

                units = int(units_str)

            except ValueError:

                print(f"Invalid unit format for customer: {name}")
                print("." * 50)

                continue


            # Billing calculation check
            try:

                bill_amt = calculate_bill(units)

                print(f"{name:^20}| {units:^10} | {'₹':>2}{bill_amt:.2f}")
                print("." * 50)

            except ValueError as error:

                print(f"Error for customer {name}: Units cannot be negative.")
                separator(50, ".")

                continue


except FileNotFoundError:

    print("Error: Customer file not found.")