start_number = int(input())
finish_number = int(input())

for number in range(start_number, finish_number+1):
    sum_odd = 0
    sum_even = 0
    for index, value in enumerate(str(number)):
        if index % 2 == 0:
            sum_even += int(value)
        else:
            sum_odd += int(value)
    if sum_even == sum_odd:
        print(number, end=" ")
print()
