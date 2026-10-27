from sys import maxsize
winner_points = - maxsize
winner_player = ""

while True:
    name_player = input()
    if name_player == "Stop":
        break
    length_name = len(name_player)
    points = 0
    for index in range(length_name):
        number = int(input())
        temp_number_name = ord(name_player[index])
        if number == temp_number_name:
            points += 10
        else:
            points += 2
    if winner_points <= points:
        winner_points = points
        winner_player = name_player

print(f"The winner is {winner_player} with {winner_points} points!")

