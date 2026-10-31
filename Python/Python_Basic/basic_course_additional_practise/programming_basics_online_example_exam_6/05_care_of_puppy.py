buy_food = float(input()) * 1000
is_Adopt = False
total_eat_food = 0

while True:
    eat_food = input()
    if eat_food == "Adopted":
        break

    eat_food_int = int(eat_food)
    total_eat_food += eat_food_int

diff_food = buy_food - total_eat_food
if diff_food >= 0:
    print(f"Food is enough! Leftovers: {diff_food:.0f} grams.")
else:
    print(f"Food is not enough. You need {abs(diff_food):.0f} grams more.")

