# Utility Billing Analytics - Version 6

## Objective
Built a modular Python-based utility billing system that calculates electricity bills and generates insights based on the data provided. It also tracks due date, payment status, and alerts in case of overdue

## Features
- Multi-column csv file to get varied data
- Reads customer data from CSV file & calculates bill
- Handles errors for missing files and invalid data
- Modular code structure (separation of logic, config, and execution)
- Presents analytics like average consumption, max/min bills, etc
- Generates insights based on due date, payment status, and more
- Removed tests folder to streamline process

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

=================================================================
             UTILITY BILLING ANALYTICS REPORT
=================================================================

###[ Revenue Analytics ]
- Total Revenue           : ₹199047.00
- Average Bill            : ₹2653.96
- Paid Revenue            : ₹92102.00
- Pending Revenue         : ₹106945.00

###[ Consumption Analytics ]
- Average Consumption     : 334.52 kWh
- High Usage Customers    : 25
- Medium Usage Customers  : 31
- Low Usage Customers     : 19
- Extreme Usage Customers : 2

###[ Billing Extremes ]
- Highest Bill            : ₹9200.00
- Highest Paying Customer : Rohan Bedi
- Lowest Bill             : ₹190.00
- Lowest Paying Customer  : Isha Malhotra

###[ Payment Monitoring ]
- Paid Customers          : 52
- Pending Customers       : 23
- Overdue Customers       : 23

###[ Customer Categories ]
- Residential Customers   : 37
- Commercial Customers    : 19
- Industrial Customers    : 19

###[ System Insights ]
- • Majority customers are medium usage consumers.
- • Most customers have completed payments.
- • Industrial customers generate the highest revenue.
- • There are 23 overdue customers who may require follow-up.

=================================================================
               END OF ANALYTICS REPORT
=================================================================