def move(r, c, curr_command):
    rd, cd = directions[curr_command]
    return r + rd, c + cd

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

n, m = (int(x) for x in input().split())
grid = []
blind_position = None
touched = 0
moves = 0
NUMBER_OF_PLAYERS = 3

for row in range(n):
    grid.append(input().split())
    for col in range(m):
        if grid[row][col] == "B":
            blind_position = (row, col)
            grid[row][col] = "-"

while True:
    command = input()
    if command == "Finish" or touched == NUMBER_OF_PLAYERS:
        break
    row, col = move(*blind_position, command)
    if not (0 <= row < n and 0 <= col < m):
        continue
    data_cell = grid[row][col]
    if data_cell == "O":
        continue
    if data_cell == "P":
        touched += 1
        grid[row][col] = "-"
    moves += 1
    blind_position = (row, col)

print("Game over!")
print(f"Touched opponents: {touched} Moves made: {moves}")
