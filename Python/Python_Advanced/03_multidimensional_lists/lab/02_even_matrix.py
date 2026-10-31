n = int(input())

my_matrix = []

my_matrix = [[int(col) for col in input().split(", ") if int(col) % 2 == 0] for row in range(n)]

print(my_matrix)