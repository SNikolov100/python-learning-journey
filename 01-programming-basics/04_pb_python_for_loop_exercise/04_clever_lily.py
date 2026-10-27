STEAL_MONEY = 1

age_lili = int(input())
price_washing_machine = float(input())
price_toy = int(input())

receive_toys = 0
receive_money = 0
even_money = 0

for age in range(1, age_lili+1):
    if age % 2 == 0:
        even_money += 10
        receive_money += even_money - STEAL_MONEY
    else:
        receive_toys += 1

total_money = receive_money + (receive_toys * price_toy)
enough_money = total_money - price_washing_machine

if enough_money >= 0:
    print(f"Yes! {enough_money:.2f}")
else:
    print(f"No! {abs(enough_money):.2f}")
