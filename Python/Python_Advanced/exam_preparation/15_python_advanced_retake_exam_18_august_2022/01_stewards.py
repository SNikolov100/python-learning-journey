from collections import deque

seats = input().split(", ")
first_line = deque(int(x) for x in input().split(", "))
second_line = [int(x) for x in input().split(", ")]
set_matches = []
rotation = 0

while len(set_matches) < 3 and rotation < 10 and first_line and second_line:
    find_seat = False
    first_el = first_line.popleft()
    last_el = second_line.pop()
    sum_el = first_el + last_el
    ascii_el = chr(sum_el)
    rotation += 1
    for data in seats:
        number = ""
        letter = ""
        for ch in data:
            if ch.isdigit():
                number += ch
            else:
                letter += ch
        if letter == ascii_el:
            if int(number) in (first_el, last_el):
                seats.remove(number + letter)
                set_matches.append(data)
                find_seat = True
                break
    if not find_seat:
        first_line.append(first_el)
        second_line.insert(0, last_el)

print(f"Seat matches: {', '.join(set_matches)}")
print(f"Rotations count: {rotation}")
