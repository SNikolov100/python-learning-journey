budget = float(input())
sell_product = 0
total_sell_price = 0
count_product = 0
is_not_enough = False

while True:
    name_product = input()
    if name_product == "Stop":
        break

    price_product = float(input())
    count_product += 1
    total_sell_price += price_product
    if count_product % 3 == 0:
        total_sell_price -= price_product / 2

    if total_sell_price > budget:
        count_product -= 1
        is_not_enough = True
        break

if is_not_enough:
    print(f"You don't have enough money!\nYou need {total_sell_price - budget:.2f} leva!")
else:
    print(f"You bought {count_product} products for {total_sell_price:.2f} leva.")