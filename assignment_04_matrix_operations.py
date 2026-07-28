# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
# (comments unchanged from scaffold)
# =============================================================================
# YOUR CODE BELOW
# =============================================================================

def read_matrix(rows, cols, label=""):
    """Read a matrix of given size from the user, row by row."""
    matrix = []
    for i in range(rows):
        row_input = input(f"Enter row {i + 1}{label}: ")
        row = [float(x) for x in row_input.split()]
        if len(row) != cols:
            print(f"Error: Expected {cols} values, got {len(row)}.")
            return None
        matrix.append(row)
    return matrix


def display_matrix(matrix, title="Matrix"):
    """Print a matrix in a neat, aligned grid format."""
    print(f"\n{title}:")
    for row in matrix:
        print("  ".join(f"{val:g}" for val in row))


def transpose_matrix(matrix):
    """Return the transpose of a matrix using nested loops."""
    rows = len(matrix)
    cols = len(matrix[0])

    result = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]

    return result


def add_matrices(matrix_a, matrix_b):
    """Return the element-wise sum of two same-sized matrices."""
    rows = len(matrix_a)
    cols = len(matrix_a[0])

    result = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix_a[i][j] + matrix_b[i][j]

    return result


def multiply_matrices(matrix_a, matrix_b):
    """Return the matrix product of A (MxN) and B (NxP)."""
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])

    result = [[0] * cols_b for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += matrix_a[i][k] * matrix_b[k][j]
            result[i][j] = total

    return result


def main():
    # ----- PART A: Transpose -----
    print("=== PART A: Transpose a Matrix ===")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    matrix = read_matrix(rows, cols)
    if matrix is None:
        return

    display_matrix(matrix, "Original Matrix")
    transposed = transpose_matrix(matrix)
    display_matrix(transposed, "Transposed Matrix")

    # ----- PART B: Addition -----
    print("\n=== PART B: Add Two Matrices ===")
    add_rows = int(input("Enter number of rows for both matrices: "))
    add_cols = int(input("Enter number of columns for both matrices: "))

    print("Matrix A:")
    matrix_a = read_matrix(add_rows, add_cols)
    if matrix_a is None:
        return

    print("Matrix B:")
    matrix_b = read_matrix(add_rows, add_cols)
    if matrix_b is None:
        return

    sum_result = add_matrices(matrix_a, matrix_b)
    display_matrix(matrix_a, "Matrix A")
    display_matrix(matrix_b, "Matrix B")
    display_matrix(sum_result, "Sum (A + B)")

    # ----- PART C: Multiplication -----
    print("\n=== PART C: Multiply Two Matrices ===")
    m = int(input("Enter rows of Matrix A: "))
    n = int(input("Enter columns of Matrix A (= rows of Matrix B): "))
    p = int(input("Enter columns of Matrix B: "))

    print("Matrix A:")
    mat_a = read_matrix(m, n)
    if mat_a is None:
        return

    print("Matrix B:")
    mat_b = read_matrix(n, p)
    if mat_b is None:
        return

    product = multiply_matrices(mat_a, mat_b)
    display_matrix(mat_a, "Matrix A")
    display_matrix(mat_b, "Matrix B")
    display_matrix(product, "Product (A x B)")


if __name__ == "__main__":
    main()