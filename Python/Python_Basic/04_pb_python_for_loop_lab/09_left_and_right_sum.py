input_number = int(input())

sum_left = 0
sum_right = 0
for inx in range(input_number * 2):
    number = int(input())
    if inx < input_number:
        sum_left += number
    else:
        sum_right += number
if sum_right == sum_left:
    print(f"Yes, sum = {sum_left}")
else:
    print(f"No, diff = {abs(sum_left - sum_right)}")

