day_of_the_week = int(input())
date = ""

if day_of_the_week == 1:
    date = "Monday"
elif day_of_the_week == 2:
    date = "Tuesday"
elif day_of_the_week == 3:
    date = "Wednesday"
elif day_of_the_week == 4:
    date = "Thursday"
elif day_of_the_week == 5:
    date = "Friday"
elif day_of_the_week == 6:
    date = "Saturday"
elif day_of_the_week == 7:
    date = "Sunday"
else:
    date = "Error"

print (date)