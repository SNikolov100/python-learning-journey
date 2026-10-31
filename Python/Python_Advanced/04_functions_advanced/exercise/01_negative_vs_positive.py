def sum_positive_and_negative(*args):
    sum_positive = 0
    sum_negative = 0
    for num in args:
        if num > 0:
            sum_positive += num
        elif num < 0:
            sum_negative += num
    return sum_positive, sum_negative

numbers = map(int, input().split())

sum_pos, sum_neg = sum_positive_and_negative(*numbers)

print(sum_neg)
print(sum_pos)
if abs(sum_neg) > sum_pos:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")