import csv

# Load data from csv
with open('cramers_matrix.csv', mode='r') as file:
    rows = list(csv.reader(file))

# skip row 0 (the header) and take start taking data
data_rows = rows[1:]
num_rows = len(data_rows)

# 2x2 Matrix A (Cols 0 & 1)
if num_rows == 2:
    A = [[float(row[0]), float(row[1])] for row in data_rows]

# 3x3 Matrix A (Cols 0, 1 & 2)
elif num_rows == 3:
    A = [[float(row[0]), float(row[1]), float(row[2])] for row in data_rows]

# Matrix B (Col 3)
B = [[float(row[3])] for row in data_rows]



# function section

# printing matrix
def print_matrix(matrix):
    for row in matrix:
        for value in row:
            print(f"{value:6.2f}", end="   ")
        print()

# determinant
def determinant(matrix):
    n = len(matrix)
    
    # for 2x2
    if n == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

    # for 3x3
    else:
        return ((matrix[0][0] *( (matrix[1][1]*matrix[2][2]) - (matrix[1][2]*matrix[2][1]) ) ) - (matrix[0][1] *( (matrix[1][0]*matrix[2][2]) - (matrix[1][2]*matrix[2][0]) ) ) + (matrix[0][2] *( (matrix[1][0]*matrix[2][1]) - (matrix[1][1]*matrix[2][0]) ) ))
    
# generating variable matrix (for x/y/z )
def var_matrix(matrix, col):
    var_M = [row[:] for row in matrix] # generatign deep copy 

    n = len(matrix)
    col-=1

    for i in range(0,n):
        var_M [i][col] = B[i][0]

    return var_M



# output section
print(f"Detected Size: {num_rows}x{num_rows}\n")

print("=> Matrix A:")
print_matrix(A)
det_A = determinant(A)
print(f"-> det(A): {det_A}")

if det_A == 0:
    print("\n=> cramer's rule can't be applied as det_A is 0 ")
    
else:
    print("\n=> Matrix B:")
    print_matrix(B)

    X = var_matrix(A,1)
    print("\nMatrix X:")
    print_matrix(X)
    det_X = determinant(X)
    print(f"-> det(X): {det_X:.2f}")

    Y = var_matrix(A,2)
    print("\n=> Matrix Y:")
    print_matrix(Y)
    det_Y = determinant(Y)
    print(f"-> det(Y): {det_Y:.2f}")

    if 3 == len(A):
        Z = var_matrix(A,3)
        print("\n=> Matrix Z:")
        print_matrix(Z)
        det_Z = determinant(Z)
        print(f"-> det(Z): {det_Z:.2f}")

    print("\n=> value of variables:")
    print(f"x = {det_X/det_A:.2f}")
    print(f"y = {det_Y/det_A:.2f}")

    if 3 == len(A):
        print(f"z = {det_Z/det_A:.2f}")