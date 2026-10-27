PREMIERE = 12
NORMAL = 7.50
DISCOUNT = 5.00

type_cinema = input()
rows = int(input())
columns = int(input())

price_ticket = ""

if type_cinema == "Premiere":
    price_ticket = PREMIERE
elif type_cinema == "Normal":
    price_ticket = NORMAL
elif type_cinema == "Discount":
    price_ticket = DISCOUNT

sum_price = price_ticket * (rows * columns)
print(type_cinema)
print(f"{sum_price:.2f} leva")
