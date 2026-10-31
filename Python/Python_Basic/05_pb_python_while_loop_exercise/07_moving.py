BOX = 1
wide_free_space = int(input())
length_free_space = int(input())
high_free_space = int(input())

size_room = int(wide_free_space * length_free_space * high_free_space)
is_Done = False
size_boxes = 0
count_boxes = 0

while size_boxes <= size_room:
    data_boxes = input()
    if data_boxes == "Done":
        is_Done = True
        break

    count_boxes = int(data_boxes)
    size_boxes += (count_boxes * BOX)

if size_boxes > size_room:
    print(f"No more free space! You need {size_boxes - size_room} Cubic meters more.")
else:
    print(f"{size_room - size_boxes} Cubic meters left.")


