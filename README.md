# Utility Billing Analytics - Day 4

## Objective
Built a modular Python-based utility billing system that calculates electricity bills using slab-based pricing, processes multiple customers from CSV files, and generates structured output in the terminal. Structured folders and files for accessibility and ease of modifications.

## Features
- Reads customer data from CSV file & calculates bill
- Handles errors for missing files and invalid data
- f-string formatting in terminal to present data
- Modular code structure (separation of logic, config, and execution)
- Configurable rates and slab limits via `config.py`
- basic test scripts for validation

## Configuration

### Slab Rates

- 0-100 units → ₹5/unit
- 101-300 units → ₹7/unit
- Above 300 units → ₹10/unit

### Fixed Charge

₹100 (added to every bill)

### Data Storage

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

- Aarav Sharma → 47 units → ₹335.00

- Rahul Verma → 251 units → ₹1657.00

- Sneha Kapoor → 318 units → ₹2280.00

### Error messages 

- negative values → Invalid data for customer 'Divya Thomas'. Skipping this entry.
- Non-Interger → Invalid unit format for customer: Ananya Iyer
- Missing value → Skipping invalid row: missing customer name or units.
- Missing file → Error: Customer file not found.