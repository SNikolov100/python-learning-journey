direction ={
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

def move_in_direction(r, c, curr_command):
    rd, cd = direction[curr_command]
    return r + rd, c + cd

def is_valid_index(r, c, number):
    return 0 <= r < number and 0 <= c < number


old_position = None
ship_position = None
meteorites = set()
resources = set()
planet_b = None
grid_space = []
units = 100
result = None
n = int(input())

for row in range(n):
    grid_space.append(input().split())
    for col in range(n):
        if grid_space[row][col] == "S":
            ship_position = (row, col)
            grid_space[row][col] = "."
        elif grid_space[row][col] == "M":
            meteorites.add((row, col))
        elif grid_space[row][col] == "P":
            planet_b = (row, col)
        elif grid_space[row][col] == "R":
            resources.add((row, col))

old_position = ship_position
while True:
    if units < 5:
        result = "Mission failed! The spaceship was stranded in space."
        break
    command = input()
    row, col = ship_position
    if (row, col) not in resources:
        old_position = (row, col)
    row, col = move_in_direction(row, col, command)
    units -= 5
    if not is_valid_index(row, col, n):
        ship_position = old_position
        result = "Mission failed! The spaceship was lost in space."
        break
    ship_position = (row, col)
    if (row, col) in resources:
        units = min(100, units + 10)
        continue
    if (row, col) in meteorites:
        units -= 5
        grid_space[row][col] = "."
        meteorites.remove((row, col))
        continue
    if (row, col) == planet_b:
        result = f"Mission accomplished! The spaceship reached Planet B with {units} resources left."
        break

if ship_position != planet_b:
    row, col = ship_position
    grid_space[row][col] = "S"
print(result)
for row in grid_space:
    print(' '.join(row))
