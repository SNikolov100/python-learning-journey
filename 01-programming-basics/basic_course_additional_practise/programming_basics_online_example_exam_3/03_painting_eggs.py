LARGE_RED = 16
LARGE_GREEN = 12
LARGE_YELLOW = 9
MEDIUM_RED = 13
MEDIUM_GREEN = 9
MEDIUM_YELLOW = 7
SMALL_RED = 9
SMALL_GREEN = 8
SMALL_YELLOW = 5

type_eggs = input()
color_eggs = input()
number_eggs = int(input())

total_sum = 0

if type_eggs == "Large":
    if color_eggs == "Red":
        total_sum = number_eggs * LARGE_RED
    elif color_eggs == "Green":
        total_sum = number_eggs * LARGE_GREEN
    elif color_eggs == "Yellow":
        total_sum = number_eggs * LARGE_YELLOW

elif type_eggs == "Medium":
    if color_eggs == "Red":
        total_sum = number_eggs * MEDIUM_RED
    elif color_eggs == "Green":
        total_sum = number_eggs * MEDIUM_GREEN
    elif color_eggs == "Yellow":
        total_sum = number_eggs * MEDIUM_YELLOW

elif type_eggs == "Small":
    if color_eggs == "Red":
        total_sum = number_eggs * SMALL_RED
    elif color_eggs == "Green":
        total_sum = number_eggs * SMALL_GREEN
    elif color_eggs == "Yellow":
        total_sum = number_eggs * SMALL_YELLOW

total_sum -= total_sum * 0.35

print(f"{total_sum:.2f} leva.")


