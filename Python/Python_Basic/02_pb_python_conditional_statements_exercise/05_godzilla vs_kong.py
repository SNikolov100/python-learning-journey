DECOR_PERCENT = 0.1
DISCOUNT_CLOTH_PERCENT = 0.1

budget = float(input())
statist_number = int(input())
statist_price_per_cloth = float(input())

sum_decor = budget*DECOR_PERCENT
sum_price_statist = statist_price_per_cloth * statist_number

if statist_number > 150:
    sum_price_statist -= sum_price_statist*DISCOUNT_CLOTH_PERCENT

sum_price = sum_price_statist + sum_decor
if sum_price > budget:
    print("Not enough money!")
    print(f"Wingard needs {abs(sum_price - budget):.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {abs(sum_price - budget):.2f} leva left.")