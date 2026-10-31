def move_in_direction(start_point, direct_command):
    r, c = start_point
    dr, dc = directions[direct_command]
    return r + dr, c + dc

def out_of_range_index(r, c, number):
    return (r + number) % number, (c + number) % number

n = int(input())
field_matrix = []
coordinate_bee = (0, 0)
coordinate_hive = (0, 0)
energy = 15
nectar = 0
need_nectar_to_success = 30
is_restore_energy = False

for row in range(n):
    field_matrix.append(list(input()))
    for col in range(n):
        if field_matrix[row][col] == "B":
            field_matrix[row][col] = "-"
            coordinate_bee = (row, col)
        elif field_matrix[row][col] == "H":
            coordinate_hive = (row, col)

directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
}


while True:
    command = input()
    energy -= 1
    row, col = move_in_direction(coordinate_bee, command )
    row, col = out_of_range_index(row, col, n)
    coordinate_bee = (row, col)
    if field_matrix[row][col] == "H":
        break
    if field_matrix[row][col].isdigit():
        nectar += int(field_matrix[row][col])
        field_matrix[row][col] = "-"
    if energy <= 0 and nectar > need_nectar_to_success and not is_restore_energy:
        energy = nectar - need_nectar_to_success
        nectar = need_nectar_to_success
        is_restore_energy = True
    if energy <=0:
        break

if coordinate_bee == coordinate_hive and nectar >= 30:
    print(f"Great job, Beesy! The hive is full. Energy left: {energy}")
elif coordinate_bee == coordinate_hive and nectar < 30:
    print("Beesy did not manage to collect enough nectar.")
else:
    print("This is the end! Beesy ran out of energy.")
field_matrix[row][col] = "B"
for row in field_matrix:
    print("".join(row))
