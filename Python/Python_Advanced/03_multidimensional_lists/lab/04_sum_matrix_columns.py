rows, cols = [int(i) for i in input().split(", ")]

my_matrix = [[int(x) for x in input().split()] for row in range(rows)]

for col in range(cols):
    sum_colon = 0
    for row in range(rows):
        sum_colon += my_matrix[row][col]
    print(sum_colon)
