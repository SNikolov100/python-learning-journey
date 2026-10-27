product = input()
city = input()
quantity = float(input())
price_product = 0.0


if city == "Sofia":
    if product == "coffee":
        price_product = 0.50
    elif product == "water":
        price_product = 0.80
    elif product == "beer":
        price_product = 1.20
    elif product == "sweets":
        price_product = 1.45
    elif product == "peanuts":
        price_product = 1.60
elif city == "Plovdiv":
    if product == "coffee":
        price_product = 0.40
    elif product == "water":
        price_product = 0.70
    elif product == "beer":
        price_product = 1.15
    elif product == "sweets":
        price_product = 1.30
    elif product == "peanuts":
        price_product = 1.50
elif city == "Varna":
    if product == "coffee":
        price_product = 0.45
    elif product == "water":
        price_product = 0.70
    elif product == "beer":
        price_product = 1.10
    elif product == "sweets":
        price_product = 1.35
    elif product == "peanuts":
        price_product = 1.55

price = price_product * quantity
print(price)