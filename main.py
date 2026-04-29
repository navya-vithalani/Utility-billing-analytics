
from src.analytics import generate_analytics
from src.utils import separator

data = generate_analytics("data/customers_new.csv")

print("\n" + "=" * 65)
print("             UTILITY BILLING ANALYTICS REPORT")
print("=" * 65)

# Revenue Analytics
print("\n[ Revenue Analytics ]")

print(f"Total Revenue           : ₹{data['total_revenue']:.2f}")
print(f"Average Bill            : ₹{data['average_bill']:.2f}")

print(f"Paid Revenue            : ₹{data['paid_revenue']:.2f}")
print(f"Pending Revenue         : ₹{data['pending_revenue']:.2f}")

# Consumption Analytics
print("\n[ Consumption Analytics ]")

print(f"Average Consumption     : {data['average_consumption']:.2f} kWh")

print(f"High Usage Customers    : {data['high_usage']}")
print(f"Medium Usage Customers  : {data['medium_usage']}")
print(f"Low Usage Customers     : {data['low_usage']}")

print(f"Extreme Usage Customers : {data['extreme_usage_count']}")

# Billing Extremes
print("\n[ Billing Extremes ]")

print(f"Highest Bill            : ₹{data['highest_bill']:.2f}")
print(f"Highest Paying Customer : {data['highest_customer']}")

print(f"Lowest Bill             : ₹{data['lowest_bill']:.2f}")
print(f"Lowest Paying Customer  : {data['lowest_customer']}")

# Payment Monitoring
print("\n[ Payment Monitoring ]")

print(f"Paid Customers          : {data['paid_count']}")
print(f"Pending Customers       : {data['pending_count']}")

print(f"Overdue Customers       : {data['overdue_count']}")

# Customer Categories
print("\n[ Customer Categories ]")

print(f"Residential Customers   : {data['residential_count']}")
print(f"Commercial Customers    : {data['commercial_count']}")
print(f"Industrial Customers    : {data['industrial_count']}")

# Insights
print("\n[ System Insights ]")

print(f"• {data['insight1']}")
print(f"• {data['insight2']}")
print(f"• {data['insight3']}")
print(f"• {data['insight4']}")

# Footer
print("\n" + "=" * 65)
print("               END OF ANALYTICS REPORT")
print("=" * 65 + "\n")