from sys import maxsize
number_easter_bread = int(input())
max_points = - maxsize
max_name_baker = ""

for _ in range(number_easter_bread):
    name_beaker = input()
    points = 0
    while True:
        grade_easter_bread = input()

        if grade_easter_bread == "Stop":
            break

        grade_int = int(grade_easter_bread)
        points += grade_int

    print(f"{name_beaker} has {points} points.")
    if max_points < points:
        max_points = points
        max_name_baker = name_beaker
        print(f"{name_beaker} is the new number 1!")

print(f"{max_name_baker} won competition with {max_points} points!")






