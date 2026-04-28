from billing import calculate_bill

#test 1
units = 50
bill_amt = calculate_bill(units)
print(f"The total bill for {units} units (kWh) is ₹{bill_amt} based on a rate of ₹5/unit.")

print("-" * 50)

#test 2
units = 250
bill_amt = calculate_bill(units)
print(f"The total bill for {units} units (kWh) is ₹{bill_amt} based on a rate of ₹5/unit for the first 100 units and ₹7/unit for the rest.")

print("-" * 50)

#test 3
units = 450
bill_amt = calculate_bill(units)
print(f"The total bill for {units} units (kWh) is ₹{bill_amt} based on a rate of ₹5/unit for the first 100 units, ₹7/unit for the next 200 units, and ₹10/unit for additional units.")

print("-" * 50)

#test 4
units = -10
bill_amt = calculate_bill(units)
print(f"The total bill for {units} units (kWh) is {bill_amt}")
