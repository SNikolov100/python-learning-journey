DECOR = 0.1
DISCOUNT_MORE_150 = 0.1

budget = float(input())
number_statists = int(input())
price_cloth_per_one = float(input())

price_decor = budget * DECOR
price_cloth = price_cloth_per_one * number_statists

if number_statists > 150:
    price_cloth -= price_cloth * DISCOUNT_MORE_150

sum_expense = price_decor + price_cloth

if sum_expense <= budget:
    print(f"Action!\nWingard starts filming with {budget - sum_expense:.2f} leva left.")
else:
    print(f"Not enough money!\nWingard needs {sum_expense - budget:.2f} leva more.")