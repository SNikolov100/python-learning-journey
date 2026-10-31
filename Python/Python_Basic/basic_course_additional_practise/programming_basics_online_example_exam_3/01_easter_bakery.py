price_floor = float(input())
kg_floor = float(input())
kg_sugar = float(input())
pack_eggs = int(input())
pack_yeast = int(input())

price_sugar = price_floor * 0.75
prise_pack_eggs = price_floor * 1.1
price_pack_yeast = price_sugar * 0.2

sum_floor = price_floor * kg_floor
sum_sugar = price_sugar * kg_sugar
sum_eggs = prise_pack_eggs * pack_eggs
sum_yeast = price_pack_yeast * pack_yeast

sum_price = sum_floor + sum_sugar + sum_eggs + sum_yeast
print(f"{sum_price:.2f}")
