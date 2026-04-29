from src.analytics import generate_analytics
from src.utils import separator

data = generate_analytics("data/customers.csv")


separator(60, "=")
print("BASIC UTILITY BILLING ANALYTICS REPORT")
separator(50, "=")

print("\n[ Revenue Analytics ]")
print(f"Total Revenue           : ₹{data['total_revenue']:.2f}")
print(f"Average Bill            : ₹{data['average_bill']:.2f}")

separator(50, "-")

print("\n[ Consumption Analytics ]")
print(f"Average Consumption     : {data['average_consumption']:.2f} kWh")
print(f"High Usage Customers    : {data['high_usage']}")
print(f"Medium Usage Customers  : {data['medium_usage']}")
print(f"Low Usage Customers     : {data['low_usage']}")

separator(50, "-")

print("\n[ Billing Extremes ]")
print(f"Highest Bill            : ₹{data['highest_bill']:.2f} ({data['highest_customer']})")
print(f"Lowest Bill             : ₹{data['lowest_bill']:.2f} ({data['lowest_customer']})")

separator(50, "-")

print("\n[ System Insights ]")
print(f"• {data['insight1']}")

print("\n" + "=" * 60)
