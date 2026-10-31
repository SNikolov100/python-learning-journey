DISCOUNT_10_15 = 0.15
DISCOUNT_16_20 = 0.20
DISCOUNT_21 = 0.25

number_guest = int(input())
price_cuvert_one_person = float(input())
budget = float(input())
price_quest = number_guest * price_cuvert_one_person

if 10 <= number_guest <= 15:
    price_quest -= price_quest * DISCOUNT_10_15
elif 16 <= number_guest <= 20:
    price_quest -= price_quest * DISCOUNT_16_20
elif number_guest >20:
    price_quest -= price_quest * DISCOUNT_21

price_cake = budget * 0.1
total_price = price_quest + price_cake
diff = abs(budget - total_price)

if total_price > budget:
    print(f"No party! {diff:.2f} leva needed.")
else:
    print(f"It is party time! {diff:.2f} leva left.")
