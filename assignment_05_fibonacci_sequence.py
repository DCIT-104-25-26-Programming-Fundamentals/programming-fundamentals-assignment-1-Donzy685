# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
# (comments unchanged from scaffold)
# =============================================================================
# YOUR CODE BELOW
# =============================================================================

def generate_fibonacci(n):
    """
    Return a list containing the first n terms of the Fibonacci sequence.
    Uses a loop, not recursion.
    """
    if n <= 0:
        return []

    sequence = []
    a, b = 0, 1

    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b

    return sequence


def is_fibonacci(number):
    """
    Return True if 'number' appears in the Fibonacci sequence, False otherwise.
    Uses a loop, not recursion.
    """
    if number < 0:
        return False

    a, b = 0, 1

    while a <= number:
        if a == number:
            return True
        a, b = b, a + b

    return False


def main():
    # ----- PART A: Print the First N Terms -----
    n_input = input("How many terms? ")
    n = int(n_input)

    if n <= 0:
        print("Error: N must be a positive integer.")
    else:
        sequence = generate_fibonacci(n)
        sequence_str = " ".join(str(num) for num in sequence)
        print(f"Fibonacci sequence: {sequence_str}")

    # ----- PART B: Check if a Number Belongs to the Sequence -----
    number_input = input("Enter a number to check: ")
    number = int(number_input)

    if is_fibonacci(number):
        print(f"{number} is a Fibonacci number.")
    else:
        print(f"{number} is NOT a Fibonacci number.")


if __name__ == "__main__":
    main()