amount_sells = int(input())
enter_data = ""
payment_rotation = 0
count_cash = 0
count_card = 0
payment_cash = 0
payment_card = 0
finish_sells = False


while True:
    enter_data = input()
    payment_rotation += 1
    if enter_data == "End":
        break

    payment = int(enter_data)

    if payment_rotation == 1:
        payment_rotation -= 2

        if payment > 100:
            print(f"Error in transaction!")
        else:
            count_cash += 1
            payment_cash += payment
            print(f"Product sold!")

    else:

        if payment < 10:
            print(f"Error in transaction!")
        else:
            count_card += 1
            payment_card += payment
            print(f"Product sold!")

    if amount_sells <= (payment_card + payment_cash):
        finish_sells = True
        break

if finish_sells:
    print(f"Average CS: {payment_cash/count_cash:.2f}")
    print(f"Average CC: {payment_card/count_card:.2f}")
else:
    print(f"Failed to collect required money for charity.")
