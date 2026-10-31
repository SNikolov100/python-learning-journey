from math import ceil
ONE_BEER = 1.20
ONE_CHIPS = 0.45

name_fen = input()
budget = float(input())
number_beers = int(input())
number_chips = int(input())

total_price_beer = number_beers * ONE_BEER
price_one_chips = total_price_beer * ONE_CHIPS
total_price_chips = ceil(price_one_chips * number_chips)

total_price = total_price_beer + total_price_chips
diff = budget - total_price

if diff >= 0:
    print(f"{name_fen} bought a snack and has {diff:.2f} leva left.")
else:
    print(f"{name_fen} needs {abs(diff):.2f} more leva!")
