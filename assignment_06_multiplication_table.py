# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
# (comments unchanged from scaffold)
# =============================================================================
# YOUR CODE BELOW
# =============================================================================

def print_table(number):
    """Print the multiplication table for a single number, 1 to 12."""
    print(f"Multiplication Table for {number}:")
    for i in range(1, 13):
        print(f"{number}  x  {i:<2} = {number * i}")


def print_tables_up_to_n(n):
    """Print multiplication tables for every number from 1 to n,
    separated by a line of dashes."""
    for num in range(1, n + 1):
        print_table(num)
        print("-" * 29)


def main():
    # ----- PART A: Single Table -----
    single_input = input("Enter a number: ")
    single_number = int(single_input)

    print_table(single_number)

    # ----- PART B: Tables from 1 to N -----
    print()
    n_input = input("Enter N (to print tables from 1 to N): ")
    n = int(n_input)

    if n <= 0:
        print("Error: N must be a positive integer.")
    else:
        print_tables_up_to_n(n)


if __name__ == "__main__":
    main()