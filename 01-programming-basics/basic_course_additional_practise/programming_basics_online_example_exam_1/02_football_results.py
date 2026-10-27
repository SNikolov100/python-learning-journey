win = 0
lost = 0
equal = 0
left = ""
right = ""

for _ in range(3):
    result = input()

    left, right = result.split(":")
    if left == right:
        equal += 1
    elif int(left) > int(right):
        win += 1
    elif int(left) < int(right):
        lost += 1

print(f"Team won {win} games.")
print(f"Team lost {lost} games.")
print(f"Drawn games: {equal}")
