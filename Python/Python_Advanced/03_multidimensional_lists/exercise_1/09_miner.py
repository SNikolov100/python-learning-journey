from collections import deque

direction = {
    "left": -1,
    "right": 1,
    "up": -1,
    "down": 1
}

def step_by_step(matr_field, player, comm):
    x, y = player[0], player[1]
    if comm == "up" or comm == "down":
        if 0<= x + direction[comm] < len(matr_field):
            x += direction[comm]
    if comm == "left" or comm == "right":
        if 0 <= y + direction[comm] < len(matr_field):
            y += direction[comm]
    player = (x, y)
    return player

n = int(input())
commands = deque(input().split())
field = []
player_position = None
end_position = None
coal = set()

for row in range(n):
    field.append(input().split())
    for col in range(n):
        if field[row][col] == "s":
            player_position = (row, col)
        if field[row][col] == "e":
            end_position = (row, col)
        if field[row][col] == "c":
            coal.add((row, col))

while True:
    if player_position == end_position:
        print(f"Game over! ({player_position[0]}, {player_position[1]})")
        break
    elif not coal:
        print(f"You collected all coal! ({player_position[0]}, {player_position[1]})")
        break
    elif not commands:
        print(f"{len(coal)} pieces of coal left. ({player_position[0]}, {player_position[1]})")
        break
    player_position = step_by_step(field, player_position, commands.popleft())

    if player_position in coal:
        coal.remove(player_position)

