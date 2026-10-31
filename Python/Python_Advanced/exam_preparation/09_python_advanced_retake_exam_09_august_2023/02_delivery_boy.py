
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

def move_in_direction(r, c, curr_command):
    rd, cd = directions[curr_command]
    return r + rd, c + cd

def in_border(r, c, max_row, max_col):
    return 0 <= r < max_row and 0 <= c < max_col

n, m = (int(x) for x in (input().split()))
grid = []
boy_position = None
restaurant_position = None
address_position = None
obstacles = set()
road = set()
start_position = None
out_of_range = False
taken_pizza = False

for row in range(n):
    grid.append(list(input()))
    for col in range(m):
        if grid[row][col] == "-":
            road.add((row, col))
        elif grid[row][col] == "B":
            boy_position = (row, col)
        elif grid[row][col] == "A":
            address_position = (row, col)
        elif grid[row][col] == "P":
            restaurant_position = (row, col)
        elif grid[row][col] == "*":
            obstacles.add((row, col))

start_position = boy_position
while True:
    command = input()
    row, col = boy_position
    row, col = move_in_direction(row, col, command)
    if not in_border(row, col, n, m):
        start_r, start_c = start_position
        grid[start_r][start_c] = " "
        out_of_range = True
        break
    else:
        if (row, col) == restaurant_position:
            grid[row][col] = "R"
            restaurant_position = None
            taken_pizza = True
            print("Pizza is collected. 10 minutes for delivery.")
        elif (row, col) in obstacles:
            continue
        elif (row, col) == address_position and taken_pizza:
            grid[row][col] = "P"
            address_position = None
            print("Pizza is delivered on time! Next order...")
            break
        elif (row, col) in road:
            grid[row][col] = "."
            road.remove((row, col))
    boy_position = (row, col)

if out_of_range:
    print("The delivery is late. Order is canceled.")

for row in grid:
    print(''.join(row))



