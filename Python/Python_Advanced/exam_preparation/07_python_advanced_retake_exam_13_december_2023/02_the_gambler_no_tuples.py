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
win_money = 100
penalty = 200
jackpot = 100000
lost_game = False
take_jackpot = False

for row in range(n):
    field_matrix.append(list(input()))
    for col in range(n):
        if field_matrix[row][col] == "G":
            field_matrix[row][col] = "-"
            gambler_position = (row, col)

while True:
    command = input()
    if command == "end":
        break
    row, col = gambler_position
    row, col = move_in_direction(row, col, command)

    if not is_valid_index(row, col, n):
        lost_game = True
        break

    gambler_position = (row, col)
    if field_matrix[row][col] == "W":
        amount += win_money
        field_matrix[row][col] = "-"
        continue

    if field_matrix[row][col] == "P":
        amount -= penalty
        field_matrix[row][col] = "-"
        if amount <= 0:
            lost_game = True
            break
        continue

    if field_matrix[row][col] == "J":
        amount += jackpot
        field_matrix[row][col] = "-"
        take_jackpot = True
        break

row, col = gambler_position
field_matrix[row][col] = "G"

if take_jackpot:
    print("You win the Jackpot!")
    print(f"End of the game. Total amount: {amount}$")
elif not lost_game:
    print(f"End of the game. Total amount: {amount}$")
else:
    print("Game over! You lost everything!")

if amount and not lost_game:
    for row in field_matrix:
        print(''.join(row))
