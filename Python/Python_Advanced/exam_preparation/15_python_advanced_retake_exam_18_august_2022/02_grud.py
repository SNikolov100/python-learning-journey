def move(r, c, curr_command):
    rd, cd = directions[curr_command]
    return r + rd, c + cd

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

N = 6
grid = []
value = ""
for row in range(N):
    grid.append(input().split())

start_position = input()
temp_position = start_position[1:-1]
temp_position = tuple(map(int, temp_position.split(", ")))

while True:
    command = input().split(", ")
    action = command[0]
    if action == "Stop":
        break
    direction = command[1]
    if len(command) == 3:
        value = command[2]

    row, col = move(*temp_position, direction)
    temp_position = (row, col)
    cell = grid[row][col]
    if action == "Create" and cell == ".":
        grid[row][col] = value
    elif action == "Update" and cell != ".":
        grid[row][col] = value
    elif action == "Delete" and cell != ".":
        grid[row][col] = "."
    elif action == "Read" and cell != ".":
        print(grid[row][col])

for row in grid:
    print(' '.join(row))
