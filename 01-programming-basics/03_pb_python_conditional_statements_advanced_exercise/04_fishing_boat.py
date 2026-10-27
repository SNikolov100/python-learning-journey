REND_SHIP_SPRING = 3000
REND_SHIP_AUTUMN_SUMMER_ = 4200
REND_SHIP_WINTER = 2600
DISCOUNT_6 = 0.1
DISCOUNT_7_11 = 0.15
DISCOUNT_12 = 0.25
DISCOUNT_EVEN = 0.05

budget = int(input())
season = input()
count_fisher = int(input())
price_boat = 0

if season == "Spring":
    price_boat = REND_SHIP_SPRING
elif (season == "Summer") or (season == "Autumn"):
    price_boat = REND_SHIP_AUTUMN_SUMMER_
elif season == "Winter":
    price_boat = REND_SHIP_WINTER

if count_fisher <= 6:
    price_boat -= price_boat * DISCOUNT_6
elif 7 <= count_fisher <= 11:
    price_boat -= price_boat * DISCOUNT_7_11
elif count_fisher >= 12:
    price_boat -= price_boat * DISCOUNT_12

if (season != "Autumn") and (price_boat != 0) and (count_fisher % 2 == 0):
    price_boat -= price_boat * DISCOUNT_EVEN

left_money = budget - price_boat
if (left_money >= 0) and (price_boat > 0):
    print(f"Yes! You have {left_money:.2f} leva left.")
elif (left_money < 0) and (price_boat > 0):
    print(f"Not enough money! You need {abs(left_money):.2f} leva.")

