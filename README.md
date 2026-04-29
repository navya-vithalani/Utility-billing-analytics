# Utility Billing Analytics - Version 7

## Objective
Built a modular Python-based utility billing system that calculates electricity bills based on taxes, discount, late penalty,etc. It also tracks due date, payment status, and alerts in case of overdue.

## Features
- Multi-column csv file to get varied data
- Reads customer data from CSV file, calculates bill, tax, discount, and penalty
- Handles errors for missing files and invalid data
- Modular code structure (separation of logic, config, and execution)
- Presents analytics like average consumption, max/min bills, etc
- Generates insights based on due date, payment status, and more

## Configuration

### Slab Rates

- 0-100 units → ₹5/unit
- 101-300 units → ₹7/unit
- Above 300 units → ₹10/unit

### Fixed Charge

₹100 (added to every bill)

## Data Storage

Customer data is stored in a CSV file with the following fields:

- Customer id
- Customer Name
- Billing month
- Units Consumed
- Payment Status
- Customer type

## Modules & Files

- src → handles logic and reusable code. Contains billing.py(calculation), analytics.py(to generate analysis) and utils.py(helper functions)
- tests → contains multiple sample codes to test individual aspects of the project
- data → contains csv and text files to be used for analysis
- config.py → stores constant values like rates and slabs
- main.py → flow of the app which runs the final output
- .gitignore → to prevent Git from tracking, staging, or committing unnecessary files—like logs, build artifacts, or secret keys—keeping the repository clean and secure.

## Error Handling

### FileNotFoundError
Displayed when the customer CSV file is missing.

### ValueError
Displayed when invalid data is found in the CSV file.

### ValueError in row
Displayed if Units value is less than zero or non integer type

### Missing data in row
Displayed if name or units is not given

## Sample Output


             UTILITY BILLING ANALYTICS REPORT


[ Revenue Analytics ]
- Total Revenue           : ₹230531.22
- Average Bill            : ₹3073.75
- Paid Revenue            : ₹104984.72
- Pending Revenue         : ₹125546.50

[ Consumption Analytics ]
- Average Consumption     : 334.52 kWh
- High Usage Customers    : 25
- Medium Usage Customers  : 31
- Low Usage Customers     : 19
- Extreme Usage Customers : 2

[ Billing Extremes ]
- Highest Bill            : ₹10856.28
- Highest Paying Customer : Rohan Bedi
- Lowest Bill             : ₹190.28
- Lowest Paying Customer  : Isha Malhotra

[ Payment Monitoring ]
- Paid Customers          : 52
- Pending Customers       : 23
- Overdue Customers       : 23

[ Customer Categories ]
- Residential Customers   : 37
- Commercial Customers    : 19
- Industrial Customers    : 19

[ Tax, Discount, and Penalty Summary ]
- Total Tax Collected    : ₹33117.57
- Total Discounts Given  : ₹1654.35
- Total Penalties Collected : ₹21.00

[ System Insights ]
- • Majority customers are medium usage consumers.
- • Most customers have completed payments.
- • Industrial customers generate the highest revenue.
- • There are 23 overdue customers who may require follow-up.
- • The company is giving more discounts than it is collecting in penalties.
- • The company has collected a total of ₹33117.57 in taxes.
- • No rows were skipped due to data issues.

               END OF ANALYTICS REPORT