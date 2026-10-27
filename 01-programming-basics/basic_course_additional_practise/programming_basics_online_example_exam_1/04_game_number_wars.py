name_first_player = input()
name_second_player = input()
points_first_player = 0
points_second_player = 0
is_Wars = False
is_End = True
counter_end_game = 0
is_36_cards = False

while True:
    card_first_player = input()
    if card_first_player == "End of game":
        is_End = True
        break
    card_second_player = input()
    if card_second_player == "End of game":
        is_End = True
        break
    card_first_player = int(card_first_player)
    card_second_player = int(card_second_player)
    if card_first_player > card_second_player:
        points_first_player += card_first_player - card_second_player
    elif card_second_player > card_first_player:
        points_second_player += card_second_player - card_first_player
    elif card_first_player == card_second_player:
        print("Number wars!")
        card_first_player = input()
        card_second_player = input()
        if card_first_player > card_second_player:
            result = f"{name_first_player} is winner with {points_first_player} points"
            is_Wars = True
            break
        elif card_second_player > card_first_player:
            result = f"{name_second_player} is winner with {points_second_player} points"
            is_Wars = True
            break
    counter_end_game += 1
    if counter_end_game == 18:
        is_36_cards = True
        break

if is_Wars:
    print(result)
elif is_End:
    print(f"{name_first_player} has {points_first_player} points")
    print(f"{name_second_player} has {points_second_player} points")
elif is_36_cards:
    if points_first_player > points_second_player:
        print(f"{name_first_player} is winner with {points_first_player} points")
    elif points_second_player > points_first_player:
        print(f"{name_second_player} is winner with {points_second_player} points")




