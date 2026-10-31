from collections import deque
substrings = deque(input().split())
main_colors = ("red", "yellow", "blue")
secondary_colors = ("orange", "purple", "green")
result = []


while substrings:
    is_color = False
    first_string = substrings.popleft()
    last_string = substrings.pop() if substrings else ""
    for color in (first_string + last_string, last_string + first_string):
        if color in main_colors or color in secondary_colors:
            result.append(color)
            is_color = True
            break

    if not is_color:
        if len(first_string) > 1:
            substrings.insert(len(substrings) // 2, first_string[:-1])
        if len(last_string) > 1:
            substrings.insert(len(substrings) // 2, last_string[:-1])

for color in result:
    if color == "orange" and not ("red" in result and "yellow" in result):
        result.remove(color)
    elif color == "purple" and not ("red" in result and "blue" in result):
        result.remove(color)
    elif color == "green" and not ("blue" in result and "yellow" in result):
        result.remove(color)

print(result)

