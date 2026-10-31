def move_in_direction(r, c, curr_command):
    rd, cd = directions[curr_command]
    return r + rd, c + cd


def in_border(r, c, max_row, max_col):
    return 0 <= r < max_row and 0 <= c < max_col


def bunny_multiplication(r, c, max_row, max_col, bunny_set):
    for key in directions:
        new_row, new_col = move_in_direction(r, c, key)
        if in_border(new_row, new_col, max_row, max_col) and (new_row, new_col) not in bunny_set:
            grid[new_row][new_col] = "B"
            bunny_set.add((new_row, new_col))
    return


directions = {
    "L": (0, -1),
    "R": (0, 1),
    "U": (-1, 0),
    "D": (1, 0)
}

n, m = (int(x) for x in input().split())
player_position = None
bunny = set()
grid = []
is_player_win = False

for row in range(n):
    grid.append(list(input()))
    for col in range(m):
        if grid[row][col] == "P":
            player_position = (row, col)
            grid[row][col] = "."
        elif grid[row][col] == "B":
            bunny.add((row, col))

commands = [x for x in input()]

for command in commands:
    row, col = player_position
    grid[row][col] = "."
    row, col = move_in_direction(row, col, command)
    for bunny_r, bunny_c in list(bunny):
        bunny_multiplication(bunny_r, bunny_c, n, m, bunny)
    if not in_border(row, col, n, m):
        is_player_win = True
        break
    player_position = (row, col)

    if player_position in bunny:
        break
    grid[row][col] = "P"


for row in grid:
    print(''.join(row))
row, col = player_position
if is_player_win:
    print(f"won: {row} {col}")
else:
    print(f"dead: {row} {col}")
