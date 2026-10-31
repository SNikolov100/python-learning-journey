start_number_eggs = int(input())
is_Close = False
is_Finish = False
sell_eggs = 0

while True:
    buy_or_sell_eggs = input()

    if buy_or_sell_eggs == "Close":
        is_Close = True
        break

    count_eggs = int(input())

    if (count_eggs > start_number_eggs) and (buy_or_sell_eggs == "Buy"):
        is_Finish = True
        break

    if buy_or_sell_eggs == "Buy":
        start_number_eggs -= count_eggs
        sell_eggs += count_eggs
    elif buy_or_sell_eggs == "Fill":
        start_number_eggs += count_eggs

if is_Close:
    print(f"Store is closed!\n{sell_eggs} eggs sold.")

if is_Finish:
    print(f"Not enough eggs in store!\nYou can buy only {start_number_eggs}.")