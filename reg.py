import csv

X = []
Y = []

# Read CSV and build matrices
with open("data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        x1 = float(row["X1"])
        x2 = float(row["X2"])
        y  = float(row["Y"])

        X.append([1, x1, x2])
        Y.append([y])


# Transpose function
def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = []

    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        result.append(new_row)

    return result


# Matrix multiplication
def multiply(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    cols_B = len(B[0])

    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result


def get_minor(matrix, row, col):
    minor = []
    for i in range(len(matrix)):
        if i != row:
            new_row = []
            for j in range(len(matrix)):
                if j != col:
                    new_row.append(matrix[i][j])
            minor.append(new_row)
    return minor


def determinant(matrix):
    n = len(matrix)

    # Base case for 1x1
    if n == 1:
        return matrix[0][0]

    # Base case for 2x2
    if n == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

    det = 0

    for col in range(n):
        sign = (-1) ** col
        minor = get_minor(matrix, 0, col)
        det += sign * matrix[0][col] * determinant(minor)

    return det

# Inverse of matrix
def inverse(matrix):
    n = len(matrix)

    # Create augmented matrix [A | I]
    augmented = []

    for i in range(n):
        row = matrix[i] + [0]*n
        row[n+i] = 1
        augmented.append(row)

    # Perform Gauss-Jordan elimination
    for i in range(n):

        # Make pivot = 1
        pivot = augmented[i][i]
        if pivot == 0:
            raise ValueError("Matrix is not invertible")

        for j in range(2*n):
            augmented[i][j] /= pivot

        # Make other rows 0 in this column
        for k in range(n):
            if k != i:
                factor = augmented[k][i]
                for j in range(2*n):
                    augmented[k][j] -= factor * augmented[i][j]

    # Extract inverse matrix
    inverse_matrix = []
    for i in range(n):
        inverse_matrix.append(augmented[i][n:])

    return inverse_matrix

def print_matrix(matrix):
    for row in matrix:
        for value in row:
            print(f"{value:.3f}", end="   ")
        print()

# Calculations
X_trans = transpose(X)
X_trans_x_X = multiply(X_trans, X)
X_trans_x_X_inverse = inverse(X_trans_x_X)
X_trans_x_X_inverse_x_X_trans = multiply(X_trans_x_X_inverse, X_trans)
X_trans_x_X_inverse_x_X_trans_x_Y = multiply(X_trans_x_X_inverse_x_X_trans,Y)

print("Matrix X:")
print_matrix(X)

print("\nX^T:")
print_matrix(X_trans)

print("\nX^T * X:")
print_matrix(X_trans_x_X)

print("\n(X^T * X)^-1:")
print_matrix(X_trans_x_X_inverse)

print("\n(X^T X)^-1 * X^T:")
print_matrix(X_trans_x_X_inverse_x_X_trans)

print("\n((X^T X)^-1 * X^T)Y:")
print_matrix(X_trans_x_X_inverse_x_X_trans_x_Y)

coeffs = [row[0] for row in X_trans_x_X_inverse_x_X_trans_x_Y]
print("")
print(f"slope: {coeffs[0]:.3f}")
print(f"a1: {coeffs[1]:.3f}")
print(f"a2: {coeffs[2]:.3f}")
