ARGENTINA_FLAGS = 3.25
ARGENTINA_CAPS = 7.20
ARGENTINA_POSTERS = 5.10
ARGENTINA_STICKERS = 1.25
BRAZIL_FLAGS = 4.20
BRAZIL_CAPS = 8.50
BRAZIL_POSTERS = 5.35
BRAZIL_STICKERS = 1.20
CROATIA_FLAGS = 2.75
CROATIA_CAPS = 6.90
CROATIA_POSTERS = 4.95
CROATIA_STICKERS = 1.10
DENMARK_FLAGS = 3.10
DENMARK_CAPS = 6.50
DENMARK_POSTERS = 4.80
DENMARK_STICKERS = 0.90
is_enter_valid_team = True
is_enter_valid_souvenir = True
name_team = input()
total_price_souvenirs = 0

type_souvenirs = input()
number_buy_souvenirs = int(input())

if name_team not in ["Argentina", "Brazil", "Croatia", "Denmark"]:
    is_enter_valid_team = False
    print("Invalid country!")

elif type_souvenirs not in ["flags", "caps", "posters", "stickers"]:
    is_enter_valid_souvenir = False
    print("Invalid stock!")

if is_enter_valid_team and is_enter_valid_souvenir:
    if name_team == "Argentina":
        if type_souvenirs == "flags":
            total_price_souvenirs = number_buy_souvenirs * ARGENTINA_FLAGS
        elif type_souvenirs == "caps":
            total_price_souvenirs = number_buy_souvenirs * ARGENTINA_CAPS
        elif type_souvenirs == "posters":
            total_price_souvenirs = number_buy_souvenirs * ARGENTINA_POSTERS
        elif type_souvenirs == "stickers":
            total_price_souvenirs = number_buy_souvenirs * ARGENTINA_STICKERS

    elif name_team == "Brazil":
        if type_souvenirs == "flags":
            total_price_souvenirs = number_buy_souvenirs * BRAZIL_FLAGS
        elif type_souvenirs == "caps":
            total_price_souvenirs = number_buy_souvenirs * BRAZIL_CAPS
        elif type_souvenirs == "posters":
            total_price_souvenirs = number_buy_souvenirs * BRAZIL_POSTERS
        elif type_souvenirs == "stickers":
            total_price_souvenirs = number_buy_souvenirs * BRAZIL_STICKERS

    elif name_team == "Croatia":
        if type_souvenirs == "flags":
            total_price_souvenirs = number_buy_souvenirs * CROATIA_FLAGS
        elif type_souvenirs == "caps":
            total_price_souvenirs = number_buy_souvenirs * CROATIA_CAPS
        elif type_souvenirs == "posters":
            total_price_souvenirs = number_buy_souvenirs * CROATIA_POSTERS
        elif type_souvenirs == "stickers":
            total_price_souvenirs = number_buy_souvenirs * CROATIA_STICKERS

    elif name_team == "Denmark":
        if type_souvenirs == "flags":
            total_price_souvenirs = number_buy_souvenirs * DENMARK_FLAGS
        elif type_souvenirs == "caps":
            total_price_souvenirs = number_buy_souvenirs * DENMARK_CAPS
        elif type_souvenirs == "posters":
            total_price_souvenirs = number_buy_souvenirs * DENMARK_POSTERS
        elif type_souvenirs == "stickers":
            total_price_souvenirs = number_buy_souvenirs * DENMARK_STICKERS

if is_enter_valid_team and is_enter_valid_souvenir:
    print(f"Pepi bought {number_buy_souvenirs} "f"{type_souvenirs}"
         f" of {name_team}"f" for {total_price_souvenirs:.2f} lv.")



