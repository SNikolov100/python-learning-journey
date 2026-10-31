win_team_desi = 0
lost_team_desi = 0

while True:
    name_of_tournament = input()
    if name_of_tournament == "End of tournaments":
        break
    all_games_for_one_tournament = int(input())
    for number_game in range(1, all_games_for_one_tournament + 1):
        team_Desi = int(input())
        team_other = int(input())
        diff_points = abs(team_Desi - team_other)
        if team_Desi > team_other:
            print(f"Game {number_game} of tournament {name_of_tournament}: win with {diff_points} points.")
            win_team_desi += 1
        elif team_other > team_Desi:
            print(f"Game {number_game} of tournament {name_of_tournament}: lost with {diff_points} points.")
            lost_team_desi += 1

all_games_all_tournament = win_team_desi + lost_team_desi
percent_win = (win_team_desi * 100) / all_games_all_tournament
percent_lost = (lost_team_desi * 100) / all_games_all_tournament

print(f"{percent_win:.2f}% matches win")
print(f"{percent_lost:.2f}% matches lost")
