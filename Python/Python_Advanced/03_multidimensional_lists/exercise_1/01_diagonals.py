n = int(input())

my_matrix = [[int(col) for col in input().split(', ')] for _ in range(n)]
primary_diagonal= [my_matrix[i][i] for i in range(n)]
secondary_diagonal = [my_matrix[i][-i-1] for i in range(n)]

print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")
