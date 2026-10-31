money_for_vacantion = float(input())
money_available = float(input())
count_day_spend = 0
count_days = 0
is_5_row = False

while money_available < money_for_vacantion:
    action_word = input()
    amount_money = float(input())
    count_days += 1

    if action_word == "spend":
        money_available -= amount_money
        if money_available < 0:
            money_available = 0
        count_day_spend += 1

        if count_day_spend == 5:
            is_5_row = True
            break

    elif action_word == "save":
        money_available += amount_money
        count_day_spend = 0

if is_5_row:
    print(f"You can't save the money.\n{count_days}")
else:
    print(f"You saved the money for {count_days} days.")


