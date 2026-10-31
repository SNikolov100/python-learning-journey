directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

def move_in_direction(r, c, curr_command):
    rd, cd = directions[curr_command]
    return r + rd, c + cd

def is_valid_index(r, c, number):
    return 0 <= r < number and 0 <= c < number

n = int(input())
field_air = []
jet_armor = 300
jet_position = None
targets = set()
repair_stations = set()

for row in range(n):
    field_air.append(list(input()))
    for col in range(n):
        if field_air[row][col] == "J":
            field_air[row][col] = "-"
            jet_position = (row, col)
        elif field_air[row][col] == "E":
            targets.add((row, col))
        elif field_air[row][col] == "R":
            repair_stations.add((row, col))

while True:
    command = input()
    row, col = jet_position
    row, col = move_in_direction(row, col, command)

    if not is_valid_index(row, col, n):
        print("Out of matrix")
        continue

    jet_position = (row, col)

    if (row, col) in targets and len(targets) == 1:
        targets.remove((row, col))
        break

    if (row, col) in targets:
        jet_armor -= 100
        if jet_armor <= 0:
            break
        field_air[row][col] = "-"
        targets.remove((row, col))

    if (row, col) in repair_stations:
        field_air[row][col] = "-"
        repair_stations.remove((row, col))
        jet_armor = 300
        continue

field_air[row][col] = "J"

if not targets:
    print("Mission accomplished, you neutralized the aerial threat!")
else:
    print(f"Mission failed, your jetfighter was shot down! Last coordinates [{row}, {col}]!")

for row in field_air:
    print(''.join(row))


