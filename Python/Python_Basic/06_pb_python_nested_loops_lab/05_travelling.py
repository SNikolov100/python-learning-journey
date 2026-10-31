budget = 0
destination = ""
saves_money = 0

while True:
    destination = input()
    if destination == "End":
        break
    budget = float(input())
    sum_money = 0
    while True:
        saves_money = float(input())
        sum_money += saves_money
        if sum_money >= budget:
            print(f"Going to {destination}!")
            break




