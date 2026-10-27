DELAY = 15

time_hour = int(input())
time_minutes = int(input()) + DELAY

if time_minutes >= 60:
    time_minutes -= 60
    time_hour += 1
if time_hour >=24:
    time_hour -= 24

if time_minutes < 10:
    print(f"{time_hour}:0{time_minutes}")
else:
    print(f"{time_hour}:{time_minutes}")