day_of_the_week = input()

price_ticket = 0

if day_of_the_week == "Monday"\
        or day_of_the_week == "Tuesday"\
        or day_of_the_week == "Friday":
    price_ticket = 12
elif day_of_the_week == "Wednesday"\
        or day_of_the_week == "Thursday":
    price_ticket = 14
elif day_of_the_week == "Saturday"\
        or day_of_the_week == "Sunday":
    price_ticket = 16

print (price_ticket)