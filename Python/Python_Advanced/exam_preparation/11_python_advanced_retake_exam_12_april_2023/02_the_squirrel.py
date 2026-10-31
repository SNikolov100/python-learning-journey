def move_in_direction(r, c, curr_command):
    rd, cd = directions[curr_command]
    return r + rd, c + cd

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

hazelnuts = 0
grid = []
squirrel_position = None
n = int(input())
commands = tuple(x for x in input().split(", "))
game_end = None

for row in range(n):
    grid.append(list(input()))
    for col in range(n):
        if grid[row][col] == "s":
            squirrel_position = (row, col)
            grid[row][col] = "*"

for command in commands:
    row, col = squirrel_position
    row, col = move_in_direction(row, col, command)
    if 0 <= row < n and 0 <= col < n:
        squirrel_position = row, col
        data_cell = grid[row][col]
        if data_cell == "h":
            hazelnuts += 1
            grid[row][col] = "*"
            if hazelnuts == 3:
                break
        elif data_cell == "t":
            game_end = "trap"
            break
    else:
        game_end = "out"
        break

if game_end == "out":
    print("The squirrel is out of the field.")
elif game_end == "trap":
    print("Unfortunately, the squirrel stepped on a trap...")
elif hazelnuts == 3:
    print("Good job! You have collected all hazelnuts!")
elif 0<= hazelnuts < 3:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {hazelnuts}")
