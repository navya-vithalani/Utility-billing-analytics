# Utility Billing Analytics - Day 2

## Objective
Implemented slab-based pricing and other basic logics.

## Features
- Slab-wise billing calculation
- Fixed charge addition
- Input validation

## Configuration

### Slab Rates

- 0-100 units → ₹5/unit
- 101-300 units → ₹7/unit
- Above 300 units → ₹10/unit

### Fixed Charge

₹100

## Files
- billing.py → contains billing logic
- test.py → test cases for bill calculation

## Sample Outputs
50 units → ₹350 (slab 1 = 50*5 + 100)
250 units → ₹1650 (slab 2 = 100*5 + 150*7 + 100)
450 units → ₹3500 (slab 3 = 100*5 + 200*7 + 150*10 + 100)
-10 units → 'invalid input' (as per input validation)