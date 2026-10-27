price_vegetable = float(input())
price_fruit = float(input())
vegetable_kg = float(input())
fruit_kg = float(input())
euro_lev = 1 / 1.94

result_price_vegetable = (price_vegetable * vegetable_kg) * euro_lev
result_price_fruit = (price_fruit * fruit_kg) * euro_lev

print(f"{(result_price_fruit + result_price_vegetable):.2f}")
