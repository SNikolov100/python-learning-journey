def fill_the_box(height, length, width, *args):
    value = height * length * width
    temp_value = 0
    for data in args:
        if data == "Finish":
            break
        temp_value += int(data)
    if temp_value < value:
        return f"There is free space in the box. You could put {value - temp_value} more cubes."
    return f"No more free space! You have {temp_value - value} more cubes."




print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print("================================")
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print("==================================")
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))