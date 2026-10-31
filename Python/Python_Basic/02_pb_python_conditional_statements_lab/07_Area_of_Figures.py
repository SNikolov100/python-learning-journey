from math import pi
print("Enter figure (square, rectangle, circle, triangle): ", end="")
figure = input()

if figure == "square":
    side = float(input())
    area = side * side
elif figure == "rectangle":
    side_one = float(input())
    side_two = float(input())
    area = side_one * side_two
elif figure == "circle":
    radius = float(input())
    area = pi * (radius ** 2)
elif figure == "triangle":
    side = float(input())
    height = float(input())
    area = (side * height) / 2
else:
    print("Enter from the selected figures !")
    exit()
print(f"{area: .3f}")