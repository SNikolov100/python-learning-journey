sell_games = int(input())
count_hearthstone = 0
count_fornite = 0
count_overwatch = 0
count_others = 0

for _ in range(sell_games):
    name_game = input()

    if name_game == "Hearthstone":
        count_hearthstone += 1
    elif name_game == "Fornite":
        count_fornite += 1
    elif name_game == "Overwatch":
        count_overwatch += 1
    else:
        count_others += 1

total_game = count_hearthstone + count_fornite + count_overwatch + count_others
percent_hearthstone = (count_hearthstone / total_game) * 100
percent_fornite = (count_fornite / total_game) * 100
percent_overwatch = (count_overwatch / total_game) * 100
percent_others = (count_others / total_game) * 100

print(f"Hearthstone - {percent_hearthstone:.2f}%")
print(f"Fornite - {percent_fornite:.2f}%")
print(f"Overwatch - {percent_overwatch:.2f}%")
print(f"Others - {percent_others:.2f}%")