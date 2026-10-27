QUARTER_FINAL_STANDARD = 55.50
QUARTER_FINAL_PREMIUM = 105.20
QUARTER_FINAL_VIP = 118.90
SEMI_FINAL_STANDARD = 75.88
SEMI_FINAL_PREMIUM = 125.22
SEMI_FINAL_VIP = 300.40
FINAL_STANDARD = 110.10
FINAL_PREMIUM = 160.66
FINAL_VIP = 400
PICTURE_WITH_CUP = 40
UP_4000 = 0.25
UP_2500 = 0.1

stage_tournament = input()
type_ticket = input()
number_of_tickets = int(input())
picture = input()
price_tickets = 0
is_4000 = False

if stage_tournament == "Quarter final":
    if type_ticket == "Standard":
        price_tickets = number_of_tickets * QUARTER_FINAL_STANDARD
    elif type_ticket == "Premium":
        price_tickets = number_of_tickets * QUARTER_FINAL_PREMIUM
    elif type_ticket == "VIP":
        price_tickets = number_of_tickets * QUARTER_FINAL_VIP
elif stage_tournament == "Semi final":
    if type_ticket == "Standard":
        price_tickets = number_of_tickets * SEMI_FINAL_STANDARD
    elif type_ticket == "Premium":
        price_tickets = number_of_tickets * SEMI_FINAL_PREMIUM
    elif type_ticket == "VIP":
        price_tickets = number_of_tickets * SEMI_FINAL_VIP
elif stage_tournament == "Final":
    if type_ticket == "Standard":
        price_tickets = number_of_tickets * FINAL_STANDARD
    elif type_ticket == "Premium":
        price_tickets = number_of_tickets * FINAL_PREMIUM
    elif type_ticket == "VIP":
        price_tickets = number_of_tickets * FINAL_VIP


if 2500 < price_tickets <= 4000:
    price_tickets -= price_tickets * UP_2500
elif price_tickets > 4000:
    price_tickets -= price_tickets * UP_4000
    is_4000 = True

if (not is_4000) and (picture == "Y"):
    price_tickets += number_of_tickets * PICTURE_WITH_CUP

print(f"{price_tickets:.2f}")
