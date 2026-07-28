# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
# (comments unchanged from scaffold)
# =============================================================================
# YOUR CODE BELOW
# =============================================================================

def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the difference of a and b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return a divided by b, rounded to 2 decimal places.
    Returns None if b is zero."""
    if b == 0:
        return None
    return round(a / b, 2)


def modulus(a, b):
    """Return the remainder of a divided by b.
    Returns None if b is zero."""
    if b == 0:
        return None
    return a % b


def exponentiate(a, b):
    """Return a raised to the power of b."""
    return a ** b


def print_menu():
    """Display the calculator menu."""
    print("============================")
    print("     SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


def get_two_numbers():
    """Prompt for and return two numbers from the user."""
    first = float(input("Enter first number : "))
    second = float(input("Enter second number: "))
    return first, second


def format_number(value):
    """Format a number for display, dropping .0 for whole numbers."""
    if value == int(value):
        return str(int(value))
    return str(value)


def main():
    operations = {
        "1": ("+", add),
        "2": ("-", subtract),
        "3": ("*", multiply),
        "4": ("/", divide),
        "5": ("%", modulus),
        "6": ("**", exponentiate),
    }

    while True:
        print_menu()
        choice = input("Select an operation (1-7): ")

        if choice == "7":
            print("Goodbye!")
            break

        if choice not in operations:
            print("Error: Invalid choice. Please enter a number from 1 to 7.")
            print()
            continue

        symbol, operation_func = operations[choice]
        a, b = get_two_numbers()

        if choice in ("4", "5") and b == 0:
            print("Error: Cannot divide by zero.")
        else:
            result = operation_func(a, b)
            print(f"Result: {format_number(a)} {symbol} {format_number(b)} = {result}")

        print()


if __name__ == "__main__":
    main()