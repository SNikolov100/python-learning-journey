row, col = [int(x) for x in input().split(", ")]
my_matrix = []
all_sum = 0

for r in range(row):
    my_matrix.append(list(map(int, input().split(", "))))
    all_sum += sum(my_matrix[r])

print(all_sum)
print(my_matrix)

