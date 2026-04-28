def format_currency(amount):
    return f"₹{amount:.2f}"

def separator(length: int, type: str):
    print(type * length)