city = input()
sells = float(input())
commission = -1.0

range_sells_1 = 0 <= sells <= 500
range_sells_2 = 500 < sells <= 1000
range_sells_3 = 1000 < sells <= 10000
range_sells_4 = 10000 < sells

if city == "Sofia":
    if range_sells_1:
        commission = 0.05
    elif range_sells_2:
        commission = 0.07
    elif range_sells_3:
        commission = 0.08
    elif range_sells_4:
        commission = 0.12
elif city == "Varna":
    if range_sells_1:
        commission = 0.045
    elif range_sells_2:
        commission = 0.075
    elif range_sells_3:
        commission = 0.10
    elif range_sells_4:
        commission = 0.13
elif city == "Plovdiv":
    if range_sells_1:
        commission = 0.055
    elif range_sells_2:
        commission = 0.08
    elif range_sells_3:
        commission = 0.12
    elif range_sells_4:
        commission = 0.145
if commission >0:
    total_sells = commission * sells
    print(f"{total_sells:.2f}")
else:
    print("error")