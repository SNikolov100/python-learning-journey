n = int(input())
sum_numbers = 0
average_numbers = 0

for _ in range(1, n+1):
    number = int(input())
    sum_numbers += number

average_numbers = sum_numbers / n
print(f"{average_numbers:.2f}")
