name_player = input()
sum_points = 301
successful_shot = 0
unsuccessful_shot = 0
is_End_games = False

while True:
    area = input()
    if area == "Retire":
        break

    current_points = int(input())
    if area == "Single":
        coeficient = 1
    elif area == "Double":
        coeficient = 2
    elif area == "Triple":
        coeficient = 3
    if sum_points >= current_points * coeficient:
        sum_points -= current_points * coeficient
        successful_shot += 1
    else:
        unsuccessful_shot += 1
    if sum_points == 0:
        is_End_games = True
        break

if is_End_games:
    print(f"{name_player} won the leg with {successful_shot} shots.")
else:
    print(f"{name_player} retired after {unsuccessful_shot} unsuccessful shots.")




