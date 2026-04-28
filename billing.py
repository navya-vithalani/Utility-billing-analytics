# Slab limits
SLAB_1 = 100
SLAB_2 = 300

# Rates per unit
RATE_1 = 5
RATE_2 = 7
RATE_EXTRA = 10

# Fixed charge
FIXED_CHARGE = 100


def calculate_bill(units):

    # Input validation
    if units < 0:
        return "Invalid input: Units cannot be negative."

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