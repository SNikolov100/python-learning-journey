def move(r, c, curr_command):
    rd, cd = directions[curr_command]
    return r + rd, c + cd

def in_border(r, c, number):
    return (r + number) % number, (c + number) % number

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

n = int(input())
grid = []
pacman_position = None
pac_health = 100
stars = set()
is_immune = False

for row in range(n):
    grid.append(list(input()))
    for col in range(n):
        if grid[row][col] == "P":
            pacman_position = (row, col)
            grid[row][col] = "-"
        elif grid[row][col] == "*":
            stars.add((row, col))

while stars and pac_health > 0:
    command = input()
    if command == "end":
        break
    row, col = move(*pacman_position, command)
    row, col = in_border(row, col, n)
    pacman_position = (row, col)
    cell = grid[row][col]
    if (row, col) in stars:
        stars.remove((row, col))
    elif cell == "F":
        is_immune = True
    elif cell == "G":
        pac_health -= 0 if is_immune else 50
        is_immune = False
    grid[row][col] = "-"

row, col = pacman_position
grid[row][col] = "P"
if pac_health == 0:
    print(f"Game over! Pacman last coordinates [{row},{col}]")
elif not stars:
    print("Pacman wins! All the stars are collected.")
else:
    print("Pacman failed to collect all the stars.")

print(f"Health: {pac_health}")
if stars:
    print(f"Uncollected stars: {len(stars)}")

for row in grid:
    print(''.join(row))