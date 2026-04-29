
from src.analytics import generate_analytics
from src.utils import separator
from src.visualisations import create_visualizations

data = generate_analytics("data/customers.csv")

separator(65, "=")
print("             UTILITY BILLING ANALYTICS REPORT")
separator(65, "=")

# Revenue Analytics
print("\n[ Revenue Analytics ]")

print(f"Total Revenue           : ₹{data['total_revenue']:.2f}")
print(f"Average Bill            : ₹{data['average_bill']:.2f}")

print(f"Paid Revenue            : ₹{data['paid_revenue']:.2f}")
print(f"Pending Revenue         : ₹{data['pending_revenue']:.2f}")

separator(65, "-")
# Consumption Analytics
print("\n[ Consumption Analytics ]")

print(f"Average Consumption     : {data['average_consumption']:.2f} kWh")

print(f"High Usage Customers    : {data['high_usage']}")
print(f"Medium Usage Customers  : {data['medium_usage']}")
print(f"Low Usage Customers     : {data['low_usage']}")

print(f"Extreme Usage Customers : {data['extreme_usage_count']}")

separator(65, "-")
# Billing Extremes
print("\n[ Billing Extremes ]")

print(f"Highest Bill            : ₹{data['highest_bill']:.2f}")
print(f"Highest Paying Customer : {data['highest_customer']}")

print(f"Lowest Bill             : ₹{data['lowest_bill']:.2f}")
print(f"Lowest Paying Customer  : {data['lowest_customer']}")

separator(65, "-")
# Payment Monitoring
print("\n[ Payment Monitoring ]")

print(f"Paid Customers          : {data['paid_count']}")
print(f"Pending Customers       : {data['pending_count']}")

print(f"Overdue Customers       : {data['overdue_count']}")

separator(65, "-")
# Customer Categories
print("\n[ Customer Categories ]")

print(f"Residential Customers   : {data['residential_count']}")
print(f"Commercial Customers    : {data['commercial_count']}")
print(f"Industrial Customers    : {data['industrial_count']}")

separator(65, "-")
# Tax, Discount, and Penalty Summary
print("\n[ Tax, Discount, and Penalty Summary ]")
print(f"Total Tax Collected       : ₹{data['total_tax_collected']:.2f}")
print(f"Total Discounts Given     : ₹{data['total_discounts_given']:.2f}")
print(f"Total Penalties Collected : ₹{data['total_penalties_collected']:.2f}")

separator(65, "-")
# Insights
print("\n[ System Insights ]")

print(f"• {data['insight1']}")
print(f"• {data['insight2']}")
print(f"• {data['insight3']}")
print(f"• {data['insight4']}")
print(f"• {data['insight5']}")
print(f"• {data['insight6']}")
print(f"• {data['insight7']}")
print(f"• {data['insight8']}")

# Footer
separator(65, "=")
print("               END OF ANALYTICS REPORT")
separator(65, "=")

data = generate_analytics("data/customers.csv")
create_visualizations(data)