PERCENT_TO_1000 = 0.2
PERCENT_ABOVE_2000 = 0.1

points = int(input())
bonus_points = 0

if points <= 100:
    bonus_points += 5
elif 100 < points <= 1000:
    bonus_points = points * PERCENT_TO_1000
else:
    bonus_points = points * PERCENT_ABOVE_2000
if points % 2 == 0:
    bonus_points += 1
elif (points % 10) == 5:
    bonus_points += 2

print(bonus_points)
print(points + bonus_points)