number_color_eggs = int(input())
count_red = 0
count_orange = 0
count_blue = 0
count_green = 0
color_eggs = ""
max_color_eggs = 0

for _ in range(number_color_eggs):
    color_egg = input()

    if color_egg == "red":
        count_red += 1
    elif color_egg == "orange":
        count_orange += 1
    elif color_egg == "blue":
        count_blue += 1
    elif color_egg == "green":
        count_green += 1
if (count_red > count_orange) and (count_red > count_blue) and (count_red > count_green):
    color_eggs = "red"
    max_color_eggs = count_red
elif (count_green > count_orange) and (count_green > count_blue):
    color_eggs = "green"
    max_color_eggs = count_green
elif count_orange > count_blue:
    color_eggs = "orange"
    max_color_eggs = count_orange
else:
    color_eggs = "blue"
    max_color_eggs = count_blue


print(f"Red eggs: {count_red}")
print(f"Orange eggs: {count_orange}")
print(f"Blue eggs: {count_blue}")
print(f"Green eggs: {count_green}")
print(f"Max eggs: {max_color_eggs} -> {color_eggs}")

