directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

def move_in_direction(r, c, direct):
    dr, dc = directions[direct]
    return r+ dr, c + dc

def is_valid_index(r, c, border):
    return 0<= r < border and 0 <= c < border


n = int(input())
field_matrix = []
health = 100
attack_monster = 40
health_potion = 15
player_position = None
exit_position = None
health_set = set()
monster_set = set()

for row in range(n):
    field_matrix.append(list(input()))
    for col in range(n):
        if field_matrix[row][col] == "P":
            player_position = (row, col)
            field_matrix[row][col] = "-"
        elif field_matrix[row][col] == "X":
            exit_position = (row, col)
        elif field_matrix[row][col] == "M":
            monster_set.add((row, col))
        elif field_matrix[row][col] == "H":
            health_set.add((row, col))

while True:
    command = input()
    row, col = player_position
    row, col = move_in_direction(row, col, command)
    if not is_valid_index(row, col, n):
        continue
    player_position = (row, col)
    if (row, col) in monster_set:
        health -= attack_monster
        if health <= 0:
            health = 0
            break
        else:
            field_matrix[row][col] = "-"
            monster_set.remove((row, col))
        continue

    if (row, col) in health_set:
        health = min(100, health_potion + health)
        field_matrix[row][col] = "-"
        health_set.remove((row, col))
        continue

    elif (row, col) == exit_position:
        exit_position = None
        break

field_matrix[row][col] = "P"

if health <= 0:
    print("Player is dead. Maze over!")
if not exit_position:
    print("Player escaped the maze. Danger passed!")
print(f"Player's health: {health} units")
for data in field_matrix:
    print("".join(data))
