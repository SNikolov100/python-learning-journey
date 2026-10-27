THORENES = 0.5
LUCIFER = 0.4
PROTECTOR = 0.3
TOTALDREAM = 0.2
AREA = 0.1

budget = float(input())
number_serials = int(input())
need_money = 0

for _ in range(number_serials):
    name_serial = input()
    price_per_serial = float(input())
    if name_serial == "Thrones":
        need_money += price_per_serial * ( 1 - THORENES)
    elif name_serial == "Lucifer":
        need_money += price_per_serial * ( 1 -LUCIFER)
    elif name_serial == "Protector":
        need_money += price_per_serial * (1 -PROTECTOR)
    elif name_serial == "TotalDrama":
        need_money += price_per_serial * (1 -TOTALDREAM)
    elif name_serial == "Area":
        need_money += price_per_serial * (1 -AREA)
    else:
        need_money += price_per_serial
diff = abs(budget - need_money)
if budget >= need_money:
    print(f"You bought all the series and left with {diff:.2f} lv.")
else:
    print(f"You need {diff:.2f} lv. more to buy the series!")
