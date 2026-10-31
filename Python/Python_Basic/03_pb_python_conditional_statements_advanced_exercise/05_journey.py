PRICE_SUMMER_BULGARIA = 0.30
PRICE_SUMMER_BALKANS = 0.40
PRICE_WINTER_BULGARIA = 0.70
PRICE_WINTER_BALKANS = 0.80
PRICE_EUROPE = 0.90

budget = float(input())
type_season = input()

type_vacantion = ""
price_vacation = 0
destination = ""
percent = 0

if (budget <= 100) and (type_season == "summer"):
    type_vacantion = "Camp"
    destination = "Bulgaria"
    percent = PRICE_SUMMER_BULGARIA
elif (budget <= 100) and (type_season == "winter"):
    type_vacantion = "Hotel"
    destination = "Bulgaria"
    percent = PRICE_WINTER_BULGARIA
elif (budget <= 1000) and (type_season == "summer"):
    type_vacantion = "Camp"
    destination = "Balkans"
    percent = PRICE_SUMMER_BALKANS
elif (budget <= 1000) and (type_season == "winter"):
    type_vacantion = "Hotel"
    destination = "Balkans"
    percent = PRICE_WINTER_BALKANS
elif budget > 1000:
    type_vacantion = "Hotel"
    destination = "Europe"
    percent = PRICE_EUROPE

if budget >= 0:
    price_vacation = budget * percent
    print(f"Somewhere in {destination}")
    print(f"{type_vacantion} - {price_vacation:.2f}")
