
# a_cap = (( inverse of( x_transpose * x)) * x_transpose))y


a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
a_dash = []
a_mod = []

rows = 3
columns = 3
# rows = int(input("Enter rows: "))
# columns = int(input("Enter columns: "))

# funcions list
def print_matrix():
    print("\n--- Matrix A ---")
    for i in range (rows):
        for j in range (columns):
            print(a[i][j],end=" ")
        print("")

def transpose():
    print("\n--- Transpose Of Matrix A ---")
    for i in range (rows):
        for j in range (columns):
            print(a[j][i],end=" ")
        print("")


choice = 1
while (choice != 0):

    print("\n1. Print Matrix")
    print("2. Transpose")
    print("0. Exit")
    
    print("enter your choice")
    choice = int(input("-> "))

    match choice:
        case 1: # print Matrix
            print_matrix()

        case 2: 
            transpose()

        case 0:
            print("--- Exiting ---")

        case _: # default case
            print("\ninvalid choice...X")
            print("try again...\n")