area = float(input())

price_per_m2 = 7.61
price_discount = 18

price_area = area * price_per_m2
price_area_discount = price_area * price_discount / 100
final_price = price_area - price_area_discount

print(f"The final price is: {final_price} lv.")
print(f"The discount is: {price_area_discount} lv.")