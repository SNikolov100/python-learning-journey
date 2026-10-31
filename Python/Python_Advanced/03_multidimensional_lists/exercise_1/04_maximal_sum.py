rows, cols = [int(x) for x in input().split()]
max_sum = -float("inf")
points = []
my_matrix = [[int(col) for col in input().split()] for _ in range(rows)]

for row in range(rows - 2):
    for col in range(cols - 2):
        temp_sum = 0
        for i in range(row,row + 3):
            for j in range(col, col + 3):
                temp_sum += my_matrix[i][j]
        if temp_sum > max_sum:
            max_sum = temp_sum
            points = [row, col]

print(f"Sum = {max_sum}")
for row in range(points[0], points[0] + 3):
    for col in range(points[1], points[1] + 3):
        print(my_matrix[row][col], end= " ")
    print()

