price_voucher = int(input())
price_current = 0
counter_tickets = 0
counter_purchase = 0

while True:
    price_voucher -= price_current
    if price_voucher < 0:
        break
    purchase = input()
    if purchase == "End":
        break
    symbols = len(purchase)

    if symbols > 8:
        price_current = sum([ord(char) for char in purchase[:2]])
        if (price_voucher - price_current) < 0:
            break
        counter_tickets += 1
    else:
        price_current = ord(purchase[0])
        if (price_voucher - price_current) < 0:
            break
        counter_purchase += 1

print(f"{counter_tickets}")
print(f"{counter_purchase}")

