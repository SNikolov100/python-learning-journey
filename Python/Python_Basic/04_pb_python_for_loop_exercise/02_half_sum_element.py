end_number = int(input())

sum_numbers = 0
max_number = float("-inf")
number = 0

for _ in range(end_number):
    number = int(input())
    sum_numbers += number
    if number > max_number:
        max_number = number

deference_numbers = sum_numbers - max_number

if deference_numbers == max_number:
    print(f"Yes\nSum = {deference_numbers}")
else:
    print(f"No\nDiff = {abs(max_number - deference_numbers)}")
