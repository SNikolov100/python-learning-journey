number = int(input())
answer = ""
valid_number = (100 <= number <= 200) or (number == 0)

if not valid_number:
    answer = "invalid"

print(answer)