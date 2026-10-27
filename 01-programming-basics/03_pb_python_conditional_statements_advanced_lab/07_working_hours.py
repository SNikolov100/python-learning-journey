hour_from_day = int(input())
day_of_the_week = input()
answer = ""

valid_hour = 10 <= hour_from_day <= 18
valid_day = day_of_the_week in ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

if valid_hour and valid_day:
    answer = "open"
else:
    answer = "closed"

print(answer)


