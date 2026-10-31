n = int(input())
my_matrix = [[int(col) for col in input().split()] for _ in range(n)]

sum_diagonal = sum([my_matrix[x][x] for x in range(n)])
print(sum_diagonal)