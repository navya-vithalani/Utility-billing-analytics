# Utility Billing Analytics - Day 3

## Objective
Implemented CSV-based multiple customer billing and data processing.

## Features
- Reads customer data from CSV file
- Calculates bills for multiple customers
- Error handling for missing files and invalid data
- f-string formatting in terminal to present data

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

## Files

- billing.py → contains billing logic
- test.py → reads CSV data and processes customer bills
- data/customers.csv → stores customer records

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