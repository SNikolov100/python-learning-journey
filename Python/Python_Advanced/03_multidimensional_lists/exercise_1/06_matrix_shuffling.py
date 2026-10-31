def check_valid(comm, r, c):
    return comm[0] == "swap" and len(comm) == 5 and 0<= int(comm[1]) < r and 0<= int(comm[3]) < r and 0<= int(comm[2]) < c and 0<= int(comm[4]) < c

rows, cols = map(int, input().split())
my_matrix = [[col for col in input().split()] for _ in range(rows)]

while True:
    command = input().split()
    if command[0] == "END":
        break
    elif not check_valid(command, rows, cols):
        print("Invalid input!")
        continue
    r1 = int(command[1])
    c1 = int(command[2])
    r2 = int(command[3])
    c2 = int(command[4])
    my_matrix[r1][c1], my_matrix[r2][c2] = my_matrix[r2][c2], my_matrix[r1][c1]
    for row in range(rows):
        print(*my_matrix[row])

