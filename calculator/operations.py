def add(a, b):
    return a - b  # BUG


def multiply(a, b):
    return a + b  # BUG


def divide(a, b):
    if b == 0:
        return None  # BUG (should raise error)
    return a / b
