def add_subtract(matr, comm, r, c, val):
    if 0 <= r < len(matr) and 0 <= c < len(matr):
        if comm == "Add":
            matr[r][c] += val
            return
        if comm == "Subtract":
            matr[r][c] -= val
    else:
        print("Invalid coordinates")

my_matrix = [[int(col) for col in input().split()] for row in range(int(input()))]

while True:
    line = input()
    if line == "END":
        break
    command, row, col, value = line.split()
    add_subtract(my_matrix, command, int(row), int(col), int(value))

for row in my_matrix:
    print(*row)
