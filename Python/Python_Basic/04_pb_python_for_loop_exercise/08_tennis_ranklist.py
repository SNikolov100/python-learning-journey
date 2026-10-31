from math import floor
WINNER = 2000
FINAL = 1200
SEMI_FINAL = 720

tournaments = int(input())
rang_points = int(input())
final_points = rang_points
count_winner = 0

for _ in range(tournaments):
    place_in_tournament = input()
    if place_in_tournament == "W":
        count_winner += 1
        final_points += WINNER
    elif place_in_tournament == "F":
        final_points += FINAL
    elif place_in_tournament == "SF":
        final_points += SEMI_FINAL

average_points = (final_points - rang_points) / tournaments
percent_winner = (count_winner * 100) / tournaments

print(f"Final points: {final_points}")
print(f"Average points: {floor(average_points)}")
print(f"{percent_winner:.2f}%")

