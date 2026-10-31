sum_simple_num = 0
sum_no_simple_num = 0
result = ""

while True:
    is_simple = False
    input_data = input()
    if input_data == "stop":
        break
    current_number = int(input_data)
    if current_number < 0:
        print("Number is negative.")
        continue
    for value in range(2, current_number):
        if current_number % value == 0:
            is_simple = True
    if is_simple:
        sum_simple_num += current_number
    else:
        sum_no_simple_num += current_number

print(f"Sum of all prime numbers is: {sum_no_simple_num}")
print(f"Sum of all non prime numbers is: {sum_simple_num}")