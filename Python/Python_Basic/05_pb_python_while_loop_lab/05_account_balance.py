contribution_money = input()
amount_money = 0
total_money = 0

while contribution_money != "NoMoreMoney":
    amount_money = float(contribution_money)
    if amount_money < 0:
        print("Invalid operation!")
        break
    total_money += amount_money
    print(f"Increase: {amount_money:.2f}")
    contribution_money = input()

print(f"Total: {total_money:.2f} ")



