ROOM = 18
APARTMENT = 25
PRESIDENT_APARTMENT = 35
DISCOUNT_APARTMENT_10 = 0.30
DISCOUNT_APARTMENT_10_15 = 0.35
DISCOUNT_APARTMENT_15 = 0.50
DISCOUNT_PRESIDENT_APARTMENT_10 = 0.1
DISCOUNT_PRESIDENT_APARTMENT_10_15 = 0.15
DISCOUNT_PRESIDENT_APARTMENT_15 = 0.2
RATTING_OVERCHARGE = 0.25
RATTING_DISCOUNT = 0.1

day_stay = int(input()) - 1
type_of_room = input()
ratting = input()
price = 0

if type_of_room == "room for one person":
    price = day_stay * ROOM
elif type_of_room == "apartment":
    price = day_stay * APARTMENT
    if day_stay < 10:
        price -= price * DISCOUNT_APARTMENT_10
    elif 10 <= day_stay <= 15:
        price -= price * DISCOUNT_APARTMENT_10_15
    elif day_stay > 15:
        price -= price * DISCOUNT_APARTMENT_15
elif type_of_room == "president apartment":
    price = day_stay * PRESIDENT_APARTMENT
    if day_stay < 10:
        price -= price * DISCOUNT_PRESIDENT_APARTMENT_10
    elif 10 <= day_stay <= 15:
        price -= price * DISCOUNT_PRESIDENT_APARTMENT_10_15
    elif day_stay > 15:
        price -= price * DISCOUNT_PRESIDENT_APARTMENT_15

if ratting == "positive":
    price += price * RATTING_OVERCHARGE
elif ratting == "negative":
    price -= price * RATTING_DISCOUNT

print(f"{price:.2f}")