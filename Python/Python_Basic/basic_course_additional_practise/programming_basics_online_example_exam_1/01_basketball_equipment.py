annual_fee = float(input())

basketball_shoes = annual_fee * 0.6
basketball_equip = basketball_shoes * 0.8
basketball_ball = basketball_equip / 4
basketball_accessories = basketball_ball / 5
sum_price = basketball_shoes + basketball_equip + basketball_ball + basketball_accessories + annual_fee

print(f"{sum_price:.2f}")

