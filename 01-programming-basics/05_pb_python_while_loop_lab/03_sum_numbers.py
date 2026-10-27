input_number = int(input())
sum_numbers = 0

while True:
    number = int(input())
    sum_numbers += number
    if sum_numbers >= input_number:
        break

print(sum_numbers)
