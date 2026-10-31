directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

def move_in_direction(r, c, curr_command):
    rd, cd = directions[curr_command]
    return r + rd, c + cd

def is_valid_index(r, c, number):
    return 0 <= r < number and 0 <= c < number


n = int(input())
amount = 100
field_matrix = []
gambler_position = None
win_position = set()
penalty_position = set()
win_money = 100
penalty = 200
jackpot = 100000
jackpot_positon = None
is_lost_game = False

for row in range(n):
    field_matrix.append(list(x for x in input()))
    for col in range(n):
        if field_matrix[row][col] == "W":
            win_position.add((row, col))
        elif field_matrix[row][col] == "P":
            penalty_position.add((row, col))
        elif field_matrix[row][col] == "G":
            field_matrix[row][col] = "-"
            gambler_position = (row, col)
        elif field_matrix[row][col] == "J":
            jackpot_positon = (row, col)

while True:
    command = input()
    if command == "end":
        break
    row, col = gambler_position
    row, col = move_in_direction(row, col, command)

    if not is_valid_index(row, col, n):
        is_lost_game = True
        break
    gambler_position = (row, col)
    if (row, col) in win_position:
        amount += win_money
        field_matrix[row][col] = "-"
        win_position.remove((row, col))
        continue

    if (row, col) in penalty_position:
        amount -= penalty
        field_matrix[row][col] = "-"
        penalty_position.remove((row, col))
        if amount <= 0:
            is_lost_game = True
            break
        continue

    if (row, col) == jackpot_positon:
        amount += jackpot
        break

row, col = gambler_position
field_matrix[row][col] = "G"

if gambler_position == jackpot_positon:
    print("You win the Jackpot!")
    print(f"End of the game. Total amount: {amount}$")
elif not is_lost_game:
    print(f"End of the game. Total amount: {amount}$")
else:
    print("Game over! You lost everything!")

if amount and not is_lost_game:
    for row in field_matrix:
        print(''.join(row))



