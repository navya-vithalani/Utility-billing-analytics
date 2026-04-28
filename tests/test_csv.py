import csv

with open("data/customers.csv", mode="r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:

        name = row.get("Customer Name", "").strip()
        units = row.get("Units Consumed", "").strip()

        if not name or not units:
            print("Skipping invalid row: missing customer name or units.")
            continue
        elif not units.isdigit() or int(units) < 0:
            print(f"Invalid unit format for customer: {name}")
            continue
        else:
            print(f"Customer: {name}, Units: {units}")
