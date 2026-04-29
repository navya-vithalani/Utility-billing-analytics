import config
from datetime import date

# Constants for billing calculation
SLAB_1 = config.SLAB_1
SLAB_2 = config.SLAB_2  
RATE_1 = config.RATE_1
RATE_2 = config.RATE_2
RATE_EXTRA = config.RATE_EXTRA
FIXED_CHARGE = config.FIXED_CHARGE
TAX_THRESHOLD = config.TAX_THRESHOLD
HIGH_TAX_RATE = config.HIGH_TAX_RATE
LOW_TAX_RATE = config.LOW_TAX_RATE
PENALTY_RATE = config.PENALTY_RATE
DUE_DAY = config.DUE_DAY
DISCOUNT_THRESHOLD = config.DISCOUNT_THRESHOLD
MAX_PENALTY = config.MAX_PENALTY
DISCOUNT_RATE = config.DISCOUNT_RATE

# Due date calculation
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

# late days calculation
def get_days_late(due_date):

    today = date.today()

    days_late = (today - due_date).days

    return max(days_late, 0)

# Penalty calculation
def calculate_penalty(days_late):

    if days_late <= 0:
        return 0

    penalty = days_late * PENALTY_RATE

    # Cap the penalty at the maximum allowed
    penalty = min(penalty, MAX_PENALTY)

    return penalty

# Slab calculation
def calculate_energy_charge(units):

    if units <= SLAB_1:
        return units * RATE_1
        
    elif units <= SLAB_2:
        return (SLAB_1 * RATE_1) + ((units - SLAB_1) * RATE_2)
        
    else:
        return (SLAB_1 * RATE_1) + ((SLAB_2 - SLAB_1) * RATE_2) + ((units - SLAB_2) * RATE_EXTRA)
    
# Tax calculation
def calculate_tax(subtotal):

    if subtotal > TAX_THRESHOLD:
        tax = subtotal * HIGH_TAX_RATE
    else:
        tax = subtotal * LOW_TAX_RATE

    return tax

# Discount calculation
def calculate_discount(subtotal):

    if subtotal < DISCOUNT_THRESHOLD:
        discount = subtotal * DISCOUNT_RATE  # 5% discount for bills below ₹2000
    else:
        discount = 0

    return discount

# Main bill calculation function
def calculate_bill(units):

    # Input validation
    if units < 0:
        raise ValueError("Invalid input: Units cannot be negative.")

    energy_charge = calculate_energy_charge(units)

    # bill calculation (adding fixed charge)
    subtotal = energy_charge + FIXED_CHARGE

    tax = calculate_tax(subtotal)
    
    discount = calculate_discount(subtotal)

    bill_amt = subtotal + tax - discount

    return {
        "bill_amount": round(bill_amt, 2),
        "subtotal": round(subtotal, 2),
        "tax": round(tax, 2),
        "discount": round(discount, 2),
        "energy charge": round(energy_charge, 2)
    }

# Bill status determination
def get_bill_status(units, days_late, discount, penalty):
    status = []

    # Usage category
    if units > 700:
        status.append("High Usage")

    elif units < 100:
        status.append("Low Usage")

    # Payment status
    if days_late > 0:
        status.append("Overdue")

    # Discount check
    if discount > 0:
        status.append("Discount Applied")

    # Penalty check
    if penalty > 0:
        status.append("Penalty Applied")

    # Default status
    if not status:
        status.append("Normal")

    return ", ".join(status)

# Total bill calculation with penalty
def calculate_total_bill(units, days_late):

    bill_details = calculate_bill(units)

    penalty = calculate_penalty(days_late)

    total_bill = bill_details["bill_amount"] + penalty

    bill_status = get_bill_status(units, days_late, bill_details["discount"], penalty)

    due_date = calculate_due_date(date.today().strftime("%Y-%m"))

    return {
        "total_bill": round(total_bill, 2),
        "bill_details": bill_details,
        "penalty": round(penalty, 2),
        "status": bill_status,
        "days_late": days_late,
        "units": units,
        "due_date": due_date
    }



    




