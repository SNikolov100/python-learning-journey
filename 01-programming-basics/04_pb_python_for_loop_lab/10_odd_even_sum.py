n_numbers = int(input())

sum_even = 0
sum_odd = 0
for inx in range(n_numbers):
    number = int(input())
    if inx % 2 == 0:
        sum_even += number
    else:
        sum_odd += number

if sum_odd == sum_even:
    print(f"Yes\nSum = {sum_odd}")
else:
    print(f"No\nDiff = {abs(sum_odd - sum_even)}")

