# =========================================================
# UTILITY FUNCTIONS
# =========================================================


def format_currency(amount):
    """Format amount as currency string."""
    return f"₹{amount:.2f}"


def separator(length: int, type: str):
    """Print a separator line."""
    print(type * length)