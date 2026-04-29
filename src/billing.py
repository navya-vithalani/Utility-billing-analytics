import sys
from pathlib import Path

# Add parent directory to path so config can be imported
sys.path.insert(0, str(Path(__file__).parent.parent))

import config
from datetime import date
from config import DUE_DAY

# Constants for billing calculation
SLAB_1 = config.SLAB_1
SLAB_2 = config.SLAB_2  
RATE_1 = config.RATE_1
RATE_2 = config.RATE_2
RATE_EXTRA = config.RATE_EXTRA
FIXED_CHARGE = config.FIXED_CHARGE

def calculate_bill(units):

    # Input validation
    if units < 0:
        raise ValueError("Invalid input: Units cannot be negative.")

    # Slab calculation
    if units <= SLAB_1:

        energy_charge = units * RATE_1

    elif units <= SLAB_2:
        energy_charge = (
            (SLAB_1 * RATE_1)
            + ((units - SLAB_1) * RATE_2)
        )

    else:

        energy_charge = (
            (SLAB_1 * RATE_1)
            + ((SLAB_2 - SLAB_1) * RATE_2)
            + ((units - SLAB_2) * RATE_EXTRA)
        )

    # Total bill calculation (adding fixed charge)

    bill_amt = energy_charge + FIXED_CHARGE

    return bill_amt



def calculate_due_date(billing_month):

    year, month = map(int, billing_month.split("-"))

    # Move to next month
    if month == 12:
        year += 1
        month = 1
    else:
        month += 1

    due_date = date(year, month, DUE_DAY)

    return due_date

def get_days_late(due_date):

    today = date.today()

    days_late = (today - due_date).days

    return max(days_late, 0)

