from collections import deque

def bomb_function(r, c, matr)-> list:
    value_bomb, matr[r][c] = matr[r][c], 0
    for i in range(-1, 2):
        if 0 <= (i + r) < len(matr):
            for j in range(-1, 2):
                if 0 <= (j + c) < len(matr):
                    if matr[i + r][j + c] > 0:
                        matr[i +r][j + c] -= value_bomb
    return matr


n = int(input())
my_matrix = [[int(col) for col in input().split()] for row in range(n)]
bombs = deque(input().split(" "))
sum_alive_cells = 0
counter_alive_cells = 0

while bombs:
    row_b, col_b = map(int, bombs.popleft().split(","))
    if my_matrix[row_b][col_b] <= 0:
        continue
    my_matrix = bomb_function(row_b, col_b, my_matrix)

for row in range(n):
    for col in range(n):
        if my_matrix[row][col] > 0:
            counter_alive_cells += 1
            sum_alive_cells += my_matrix[row][col]

print(f"Alive cells: {counter_alive_cells}")
print(f"Sum: {sum_alive_cells}")

for row in my_matrix:
    print(*row, sep=" ")
