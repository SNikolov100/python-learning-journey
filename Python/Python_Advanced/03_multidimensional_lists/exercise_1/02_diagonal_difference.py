n = int(input())

my_matrix = [[int(col) for col in input().split()] for _ in range(n)]
primary_diagonal = sum([my_matrix[i][i] for i in range(n)])
secondary_diagonal = sum([my_matrix[i][-i-1] for i in range(n)])
print(abs(primary_diagonal - secondary_diagonal))