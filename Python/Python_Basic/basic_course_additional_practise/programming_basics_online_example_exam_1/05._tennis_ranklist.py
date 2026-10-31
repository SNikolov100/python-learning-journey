from math import floor
WINNER = 2000
FINAL = 1200
SEMI_FINAL = 720

number_tournaments = int(input())
start_points = int(input())
tournament_points = 0
average_points = 0
winter_points = 0

for _ in range(number_tournaments):
    place_in_tour = input()

    if place_in_tour == "W":
        tournament_points += WINNER
        winter_points += 1

    elif place_in_tour == "F":
        tournament_points += FINAL

    elif place_in_tour == "SF":
        tournament_points += SEMI_FINAL

average_points = tournament_points / number_tournaments
average_wins = (winter_points / number_tournaments) * 100

print(f"Final points: {tournament_points + start_points}")
print(f"Average points: {floor(average_points):.0f}")
print(f"{average_wins:.2f}%")







