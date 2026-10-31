def move(r, c, curr_command):
    rd, cd = directions[curr_command]
    return r + rd, c + cd

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}
MAX_HITS = 3
TOTAL_CRUISER = 3
n = int(input())
grid = []
submarine_position = None
cruise = 0
hit_mine = 0

for row in range(n):
    grid.append(list(input()))
    for col in range(n):
        if grid[row][col] == "S":
            submarine_position = (row, col)
            grid[row][col] = "-"

while cruise < TOTAL_CRUISER and hit_mine < MAX_HITS:
    command = input()
    row, col = move(*submarine_position, command)
    data_cell = grid[row][col]
    if data_cell == "*":
        hit_mine += 1
    elif data_cell == "C":
        cruise += 1
    grid[row][col] = "-"
    submarine_position = (row, col)

row, col = submarine_position
grid[row][col] = "S"

if cruise == TOTAL_CRUISER:
    print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
else:
    print(f"Mission failed, U-9 disappeared! Last known coordinates [{row}, {col}]!")

for row in grid:
    print("".join(row))
