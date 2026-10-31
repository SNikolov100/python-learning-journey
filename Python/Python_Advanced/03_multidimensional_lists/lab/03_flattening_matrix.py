n = int(input())

my_matrix = []


for row in range(n):
    my_matrix.extend([int(i) for i in input().split(", ")])

print(my_matrix)