STUDIO_MAY_OCTOBER = 50
STUDIO_JUNE_SEPTEMBER = 75.20
STUDIO_JULY_AUGUST = 76
APARTMENT_MAY_OCTOBER = 65
APARTMENT_JUNE_SEPTEMBER = 68.70
APARTMENT_JULY_AUGUST = 77
DISCOUNT_STUDIO_MAY_OCTOBER_MORE_7 = 0.05
DISCOUNT_STUDIO_MAY_OCTOBER_MORE_14 = 0.3
DISCOUNT_STUDIO_JUNE_SEPTEMBER_14 = 0.2
DISCOUNT_APARTMENT_14 = 0.1

month = input()
number_overnight = int(input())
sum_payment_studio = 0
sum_payment_apartment = 0

if month in ("May", "October"):
    sum_payment_studio = STUDIO_MAY_OCTOBER * number_overnight
    sum_payment_apartment = APARTMENT_MAY_OCTOBER * number_overnight
    if 7 < number_overnight <= 14:
        sum_payment_studio -= sum_payment_studio * DISCOUNT_STUDIO_MAY_OCTOBER_MORE_7
    elif number_overnight > 14:
        sum_payment_studio -= sum_payment_studio * DISCOUNT_STUDIO_MAY_OCTOBER_MORE_14
        sum_payment_apartment -= sum_payment_apartment * DISCOUNT_APARTMENT_14
elif month in ("June", "September"):
    sum_payment_studio = STUDIO_JUNE_SEPTEMBER * number_overnight
    sum_payment_apartment = APARTMENT_JUNE_SEPTEMBER * number_overnight
    if 14 < number_overnight:
        sum_payment_studio -= sum_payment_studio * DISCOUNT_STUDIO_JUNE_SEPTEMBER_14
        sum_payment_apartment -= sum_payment_apartment * DISCOUNT_APARTMENT_14
elif month in ("July", "August"):
    sum_payment_studio = STUDIO_JULY_AUGUST * number_overnight
    sum_payment_apartment = APARTMENT_JULY_AUGUST * number_overnight
    if number_overnight > 14:
        sum_payment_apartment -= sum_payment_apartment * DISCOUNT_APARTMENT_14

print(f"Apartment: {sum_payment_apartment:.2f} lv.")
print(f"Studio: {sum_payment_studio:.2f} lv.")
