BASKET = 1.50
WREATH = 3.80
CHOCOLATE_BUNNY = 7
count_purchase_all = 0
price_purchase_all = 0

number_client = int(input())

for _ in range(number_client):
    count_purchase_temp = 0
    price_purchase_temp = 0

    while True:
        purchase = input()

        if purchase == "Finish":
            break
        count_purchase_temp += 1

        if purchase == "basket":
            price_purchase_temp += BASKET
        elif purchase == "wreath":
            price_purchase_temp += WREATH
        elif purchase == "chocolate bunny":
            price_purchase_temp += CHOCOLATE_BUNNY
    if count_purchase_temp % 2 == 0:
        price_purchase_temp -= price_purchase_temp * 0.2

    count_purchase_all += count_purchase_temp
    price_purchase_all += price_purchase_temp
    print(f"You purchased {count_purchase_temp} items for {price_purchase_temp:.2f} leva.")

average_price_per_client = price_purchase_all / number_client
print(f"Average bill per client is: {average_price_per_client:.2f} leva.")


