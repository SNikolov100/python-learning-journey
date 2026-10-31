start_interval = int(input())
finish_interval = int(input())
magic_number = int(input())
number_combination = 0
sum_numbers = 0
first_number = 0
second_number = 0
flag_combination = True

for x1 in range(start_interval, (finish_interval+1)):
    for x2 in range(start_interval, (finish_interval+1)):
        sum_numbers = x1 + x2
        number_combination += 1
        if sum_numbers == magic_number:
            flag_combination = False
            first_number = x1
            second_number = x2
            break
    if not flag_combination:
        break
if flag_combination:
    print(f"{number_combination} combinations - neither equals {magic_number}")
else:
    print(f"Combination N:{number_combination} ({first_number} + {second_number} = {magic_number})")
