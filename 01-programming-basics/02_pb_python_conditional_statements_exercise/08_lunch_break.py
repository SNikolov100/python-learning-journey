from math import ceil
LUNCH_DURATION = 1/8
RELAX_DURATION = 1/4

show_name = str(input())
show_duration = int(input())
rest_duration = int(input())

time_lunch = LUNCH_DURATION * rest_duration
time_relax = RELAX_DURATION * rest_duration
time_all = time_relax + time_lunch + show_duration

if time_all <= rest_duration:
    print(f"You have enough time to watch {show_name} and left with {ceil(abs(time_all - rest_duration))} minutes free time.")
else:
    print(f"You don't have enough time to watch {show_name}, you need {ceil(abs(time_all - rest_duration))} more minutes.")
