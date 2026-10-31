number = int(input())
answer = ""
valid = (-100 <= number <= 100) and (number != 0)

if valid:
    answer = "Yes"
else:
    answer = "No"

print(answer)