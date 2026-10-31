def collect_eggs(field_matrix, pos_bunny):
    direction = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }
    max_eggs = -float("inf")
    position_for_max_eggs = []
    max_eggs_for_direction = None
    for direct, value in direction.items():
        start_row, start_col = pos_bunny
        r, c = value
        eggs = 0
        temp_positon = []
        while True:
            new_row, new_col = start_row + r, start_col + c
            if 0<= new_row < len(field_matrix) and 0<= new_col < len(field_matrix[0]):
                if field_matrix[new_row][new_col] == "X":
                    break
                eggs += int(field_matrix[new_row][new_col])
                temp_positon.append([new_row,new_col])
                start_row, start_col = new_row, new_col
            else:
                break
        if eggs > max_eggs and temp_positon:
            max_eggs = eggs
            position_for_max_eggs = temp_positon.copy()
            max_eggs_for_direction = direct

    return position_for_max_eggs, max_eggs_for_direction, max_eggs


n = int(input())
field = []
bunny = set()
for row in range(n):
    field.append([x for x in input().split()])
    for col in range(len(field[0])):
        if field[row][col] == "B":
            bunny = (row,col)
positions, direction, max_egg = collect_eggs(field, bunny)

print(direction)
for data in positions:
    print(data)
print(max_egg)
