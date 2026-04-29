# Utility Billing Analytics - Version 5

## Objective
Built a modular Python-based utility billing system that calculates electricity bills and generates insights based on the data provided.

## Features
- Reads customer data from CSV file & calculates bill
- Handles errors for missing files and invalid data
- f-string formatting in terminal to present data
- Modular code structure (separation of logic, config, and execution)
- Presents analytics like average consumption, max/min bills, etc
- Generates insights based on low, high, and medium usage customers

## Configuration

### Slab Rates

- 0-100 units → ₹5/unit
- 101-300 units → ₹7/unit
- Above 300 units → ₹10/unit

### Fixed Charge

₹100 (added to every bill)

## Data Storage

Customer data is stored in a CSV file with the following fields:

- Customer Name
- Units Consumed

## Modules & Files

- src → handles logic and reusable code. Contains billing.py(calculation) and utils.py(helper functions)
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

## Sample Outputs

-BASIC UTILITY BILLING ANALYTICS REPORT
==================================================

-[ Revenue Analytics ]
-Total Revenue           : ₹72070.00
-Average Bill            : ₹1566.74
--------------------------------------------------

-[ Consumption Analytics ]
-Average Consumption     : 227.15 kWh
-High Usage Customers    : 3
-Medium Usage Customers  : 36
-Low Usage Customers     : 7
--------------------------------------------------

-[ Billing Extremes ]
-Highest Bill            : ₹4610.00 (Meera Joshi)
-Lowest Bill             : ₹100.00 (Aisha Khan)
--------------------------------------------------

-[ System Insights ]
-• Majority customers are medium usage consumers.

============================================================