from math import floor, ceil
OWN_DONATE = 1 / 8
SPONSOR_DONATE = 7 / 8

price_tennis_rocket = float(input())
count_tennis_rockets = int(input())
shoes = int(input())

sum_tennis_rockets = price_tennis_rocket * count_tennis_rockets
price_shoes = (1 / 6) * price_tennis_rocket
sum_shoes = price_shoes * shoes
sum_equip_price = (sum_tennis_rockets + sum_shoes) * 0.2
sum_price = sum_tennis_rockets + sum_shoes + sum_equip_price

print(f"Price to be paid by Djokovic {floor(sum_price * OWN_DONATE)}")
print(f"Price to be paid by sponsors {ceil(sum_price * SPONSOR_DONATE)}")

