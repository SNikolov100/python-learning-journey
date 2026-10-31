fruit = input()
day_of_the_week = input()
quantity = float(input())
price_fruit = -1.0

if day_of_the_week in ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday"):
    if fruit == "banana":
        price_fruit = 2.50
    elif fruit == "apple":
        price_fruit = 1.20
    elif fruit == "orange":
        price_fruit = 0.85
    elif fruit == "grapefruit":
        price_fruit = 1.45
    elif fruit == "kiwi":
        price_fruit = 2.70
    elif fruit == "pineapple":
        price_fruit = 5.50
    elif fruit == "grapes":
        price_fruit = 3.85
elif day_of_the_week in ("Saturday", "Sunday"):
    if fruit == "banana":
        price_fruit = 2.70
    elif fruit == "apple":
        price_fruit = 1.25
    elif fruit == "orange":
        price_fruit = 0.90
    elif fruit == "grapefruit":
        price_fruit = 1.60
    elif fruit == "kiwi":
        price_fruit = 3.00
    elif fruit == "pineapple":
        price_fruit = 5.60
    elif fruit == "grapes":
        price_fruit = 4.20
if price_fruit < 0:
    print("error")
else:
    total_price = price_fruit * quantity
    print(f"{total_price:.2f}")