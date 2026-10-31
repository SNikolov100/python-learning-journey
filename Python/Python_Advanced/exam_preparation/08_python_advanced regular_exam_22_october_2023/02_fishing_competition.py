directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

def move_in_direction(r, c, direct_command):
    rd, cd = directions[direct_command]
    return r + rd, c + cd

def in_border(r, c, number):
    return (r + number) % number, (c + number) % number


n = int(input())
sea_grid = []
ship = None
whirlpool = set()
quantity_fish = 0
is_sink = False
target_quota = 20

for row in range(n):
    sea_grid.append(list(input()))
    for col in range(n):
        if sea_grid[row][col] == "S":
            ship = (row, col)
            sea_grid[row][col] = "-"
        elif sea_grid[row][col] == "W":
            whirlpool = (row, col)

while True:
    command = input()
    if command == "collect the nets":
        break
    row, col = ship
    row, col = move_in_direction(row, col, command)
    row, col  = in_border(row, col, n)

    if whirlpool:
        if (row, col) == whirlpool:
            quantity_fish = 0
            is_sink = True
            ship = (row,col)
            break
    if sea_grid[row][col].isdigit():
        quantity_fish += int(sea_grid[row][col])
        sea_grid[row][col] = "-"

    ship = (row, col)

row, col = ship
sea_grid[row][col] = "S"

if is_sink:
    print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{row},{col}]")
elif quantity_fish >= 20:
    print("Success! You managed to reach the quota!")
else:
    print(f"You didn't catch enough fish and didn't reach the quota! You need {target_quota - quantity_fish} tons of fish more.")

if quantity_fish > 0:
    print(f"Amount of fish caught: {quantity_fish} tons.")

if not is_sink:
    for row in sea_grid:
        print(''.join(row))
