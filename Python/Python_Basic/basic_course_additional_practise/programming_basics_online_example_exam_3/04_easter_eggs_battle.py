player_1_eggs = int(input())
player_2_eggs = int(input())
is_Win_1 = False
is_Win_2 = False
is_End = False

while True:
    winner = input()

    if winner == "End":
        is_End = True
        break

    if winner == "one":
        player_2_eggs -= 1
    elif winner == "two":
        player_1_eggs -= 1

    if player_1_eggs == 0:
        is_Win_2 = True
        break
    elif player_2_eggs == 0:
        is_Win_1 = True
        break

if is_End:
    print(f"Player one has {player_1_eggs} eggs left.")
    print(f"Player two has {player_2_eggs} eggs left.")

elif is_Win_1:
    print(f"Player two is out of eggs. Player one has {player_1_eggs} eggs left.")

elif is_Win_2:
    print(f"Player one is out of eggs. Player two has {player_2_eggs} eggs left.")