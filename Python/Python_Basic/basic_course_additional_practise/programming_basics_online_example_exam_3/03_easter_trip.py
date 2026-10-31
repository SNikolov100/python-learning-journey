FRANCE_21_23 = 30
FRANCE_24_27 = 35
FRANCE_28_31 = 40
ITALY_21_23 = 28
ITALY_24_27 = 32
ITALY_28_31 = 39
GERMANY_21_23 = 32
GERMANY_24_27 = 37
GERMANY_28_31 = 43

destination = input()
period = input()
number_night = int(input())
total_sum = 0

if destination == "France":
    if period == "21-23":
        total_sum = number_night * FRANCE_21_23
    elif period == "24-27":
        total_sum = number_night * FRANCE_24_27
    elif period == "28-31":
        total_sum = number_night * FRANCE_28_31
elif destination == "Italy":
    if period == "21-23":
        total_sum = number_night * ITALY_21_23
    elif period == "24-27":
        total_sum = number_night * ITALY_24_27
    elif period == "28-31":
        total_sum = number_night * ITALY_28_31
elif destination == "Germany":
    if period == "21-23":
        total_sum = number_night * GERMANY_21_23
    elif period == "24-27":
        total_sum = number_night * GERMANY_24_27
    elif period == "28-31":
        total_sum = number_night * GERMANY_28_31

print(f"Easter trip to {destination} : {total_sum:.2f} leva.")