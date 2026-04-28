from billing import calculate_bill

#test 1
units = 50
bill_amt = calculate_bill(units)
print(f"The total bill for {units} units (kWh) is ₹{bill_amt} based on a rate of ₹5/unit.")

print("-" * 50)

#test 2
units = 250
bill_amt = calculate_bill(units)
print(f"The total bill for {units} units (kWh) is ₹{bill_amt} based on a rate of ₹5/unit.")
