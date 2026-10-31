input_numbers = int(input())
sum_numbers = 0
numbers_in_range_p1 = 0
numbers_in_range_p2 = 0
numbers_in_range_p3 = 0
numbers_in_range_p4 = 0
numbers_in_range_p5 = 0

for _ in range(input_numbers):
    number = int(input())
    sum_numbers += 1
    if number < 200:
        numbers_in_range_p1 += 1
    elif 200 <= number <= 399:
        numbers_in_range_p2 += 1
    elif 400 <= number <= 599:
        numbers_in_range_p3 += 1
    elif 600 <= number <= 799:
        numbers_in_range_p4 += 1
    else:
        numbers_in_range_p5 += 1
numbers_in_range_p1 = (numbers_in_range_p1 / sum_numbers) * 100
numbers_in_range_p2 = (numbers_in_range_p2 / sum_numbers) * 100
numbers_in_range_p3 = (numbers_in_range_p3 / sum_numbers) * 100
numbers_in_range_p4 = (numbers_in_range_p4 / sum_numbers) * 100
numbers_in_range_p5 = (numbers_in_range_p5 / sum_numbers) * 100

print(f"{numbers_in_range_p1:.2f}%")
print(f"{numbers_in_range_p2:.2f}%")
print(f"{numbers_in_range_p3:.2f}%")
print(f"{numbers_in_range_p4:.2f}%")
print(f"{numbers_in_range_p5:.2f}%")

