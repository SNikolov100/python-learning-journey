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

n, m = (int(x) for x in input().split(","))
grid = []
mouse_position = None
out_of_range = False
is_trapped = False
cheese_count = 0

for row in range(n):
    grid.append(list(input()))
    for col in range(m):
        data = grid[row][col]
        if data == "M":
            mouse_position = (row, col)
            grid[row][col] = "*"
        elif data == "C":
            cheese_count += 1

while True:
    command = input()
    if command == "danger":
        break
    last_row, last_col = mouse_position
    row, col = move_in_direction(*mouse_position, command)
    if not in_border(row, col, n, m):
        out_of_range = True
        break
    data = grid[row][col]
    mouse_position = (row, col)
    if data == "T":
        is_trapped = True
        break

    if data == "C":
        grid[row][col] = "*"
        cheese_count -= 1
        if cheese_count == 0:
            break
    elif data == "@":
        mouse_position = last_row, last_col

if out_of_range:
    print("No more cheese for tonight!")
elif is_trapped:
    print("Mouse is trapped!")
elif cheese_count == 0:
    print("Happy mouse! All the cheese is eaten, good night!")
elif cheese_count > 0:
    print("Mouse will come back later!")
row, col = mouse_position
grid[row][col] = "M"
for row in grid:
    print("".join(row))
