n = int(input())

my_matrix = [[ch for ch in input()] for _ in range(n)]
search_simbol = input()

for row in range(n):
    for col in range(n):
        if my_matrix[row][col] == search_simbol:
            print(f"({row}, {col})")
            exit()

print(f"{search_simbol} does not occur in the matrix")