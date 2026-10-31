def move(r, c, curr_command):
    rd, cd = directions[curr_command]
    return r + rd, c + cd

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}
n = int(input())
racing_number = input()
grid = []
car_position = (0, 0)
trace_km = 10
tunnel_km = 30
tunnel_position = set()
total_km = 0
result = None

for row in range(n):
    grid.append(input().split())
    for col in range(n):
        if grid[row][col] == "T":
            tunnel_position.add((row, col))

while True:
    command = input()
    if command == "End":
        break
    row, col = move(*car_position, command)
    if (row, col) in tunnel_position:
        tunnel_position.remove((row, col))
        grid[row][col] = "."
        (row, col) = tunnel_position.pop()
        grid[row][col] = "."
        total_km += tunnel_km
        car_position = (row, col)
        continue
    total_km += trace_km
    car_position = (row, col)
    if grid[row][col] == "F":
        result = "Win"
        break

row,col = car_position
grid[row][col] = "C"
if result == "Win":
    print(f"Racing car {racing_number} finished the stage!")
else:
    print(f"Racing car {racing_number} DNF.")

print(f"Distance covered {total_km} km.")
for row in grid:
    print(''.join(row))

