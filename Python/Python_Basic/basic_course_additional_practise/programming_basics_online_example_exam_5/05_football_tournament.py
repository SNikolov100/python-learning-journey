name_team = input()
done_games = int(input())
win_points = 0
win_games = 0
equal_games = 0
lose_games = 0

if done_games == 0:
    print(f"{name_team} hasn't played any games during this season.")
else:
    for _ in range(done_games):
        result_one_game = input()

        if result_one_game == "W":
            win_games += 1
        elif result_one_game == "D":
            equal_games += 1
        elif result_one_game == "L":
            lose_games += 1

    win_points = (3 * win_games) + (equal_games)
    percent_win_games = (win_games / done_games) * 100
    print(f"{name_team} has won {win_points} points during this season.")
    print(f"Total stats:")
    print(f"## W: {win_games}")
    print(f"## D: {equal_games}")
    print(f"## L: {lose_games}")
    print(f"Win rate: {percent_win_games:.2f}%")