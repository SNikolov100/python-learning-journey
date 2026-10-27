number = int(input())
current_number = 0
is_last = False

for row in range(1, number+1):
    for column in range(1, row+1):
        current_number += 1
        print(current_number, end=" ")
        if current_number == number:
            is_last = True
            break
    print()
    if is_last:
        break
