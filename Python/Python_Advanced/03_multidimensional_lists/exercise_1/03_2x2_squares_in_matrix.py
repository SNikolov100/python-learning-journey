rows, cols = map(int, input().split())

my_matrix = [[col for col in input().split()] for _ in range(rows)]
counter = 0

for row in range(rows-1):
    for col in range(cols-1):
        if my_matrix[row][col] == my_matrix[row+1][col] == my_matrix[row][col+1] == my_matrix[row+1][col+1]:
            counter += 1

print(counter)