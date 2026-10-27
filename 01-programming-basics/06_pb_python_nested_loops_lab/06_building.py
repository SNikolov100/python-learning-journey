floor = int(input())
room = int(input())
name_room = ""

for x in range(floor, 0, -1):
    if x == floor:
        name_room = "L"
    elif x % 2 == 0:
        name_room = "O"
    else:
        name_room = "A"
    for y in range(room):
        print(f"{name_room}{x}{y}", end=" ")
    print()