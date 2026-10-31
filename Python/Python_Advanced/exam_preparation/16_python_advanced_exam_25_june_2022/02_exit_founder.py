import ast

N = 6
grid = []
counter = 0
player_one, player_two = input().split(", ")
is_rest_player_one = False
is_rest_player_two = False

for row in range(N):
    grid.append(input().split())

while True:
    counter = 1 if counter == 2 else (counter + 1)
    command = ast.literal_eval(input())
    player = player_one if counter == 1 else player_two
    if is_rest_player_two and player == player_two:
        is_rest_player_two = False
        continue
    if is_rest_player_one and player == player_one:
        is_rest_player_one = False
        continue
    row, col = command[0], command[1]
    cell = grid[row][col]
    if cell == "E":
        print(f"{player} found the Exit and wins the game!")
        break
    if cell == "T":
        winner = player_one if counter == 2 else player_two
        print(f"{player} is out of the game! The winner is {winner}.")
        break
    if cell == "W":
        if player == player_one:
            is_rest_player_one = True
        if player == player_two:
            is_rest_player_two = True
        print(f"{player} hits a wall and needs to rest.")

