rows, cols = map(int, input().split(', '))
my_matrix = [[int(col) for col in input().split(', ')] for _ in range(rows)]
max_sum = -float("inf")
my_coordinate = []

for row in range(rows-1):
    for col in range(cols-1):
        result = my_matrix[row][col] + my_matrix[row+1][col] + my_matrix[row][col+1] + my_matrix[row+1][col+1]
        if result > max_sum:
            max_sum = result
            my_coordinate = row, col

for row in range(my_coordinate[0],my_coordinate[0]+2):
    for col in range(my_coordinate[1],my_coordinate[1]+2):
        print(my_matrix[row][col], end=' ')
    print()
print(max_sum)