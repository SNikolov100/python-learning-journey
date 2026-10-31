A_STAR_IS_BORN_NORMAL = 7.50
A_STAR_IS_BORN_LUXURY = 10.50
A_STAR_IS_BORN_ULTRA_LUXURY = 13.50
BOHEMIAN_RHAPSODY_NORMAL = 7.35
BOHEMIAN_RHAPSODY_LUXURY = 9.45
BOHEMIAN_RHAPSODY_ULTRA_LUXURY = 12.75
GREEN_BOOK_NORMAL = 8.15
GREEN_BOOK_LUXURY = 10.25
GREEN_BOOK_ULTRA_LUXURY = 13.25
THE_FAVOURITE_NORMAL = 8.75
THE_FAVOURITE_LUXURY = 11.55
THE_FAVOURITE_ULTRA_LUXURY = 13.95

name_move = input()
type_hall = input()
sell_tickets = int(input())

if (name_move == "A Star Is Born") and (type_hall == "normal"):
    sum_price = sell_tickets * A_STAR_IS_BORN_NORMAL
elif (name_move == "A Star Is Born") and (type_hall == "luxury"):
    sum_price = sell_tickets * A_STAR_IS_BORN_LUXURY
elif (name_move == "A Star Is Born") and (type_hall == "ultra luxury"):
    sum_price = sell_tickets * A_STAR_IS_BORN_ULTRA_LUXURY
elif (name_move == "Bohemian Rhapsody") and (type_hall == "normal"):
    sum_price = sell_tickets * BOHEMIAN_RHAPSODY_NORMAL
elif (name_move == "Bohemian Rhapsody") and (type_hall == "luxury"):
    sum_price = sell_tickets * BOHEMIAN_RHAPSODY_LUXURY
elif (name_move == "Bohemian Rhapsody") and (type_hall == "ultra luxury"):
    sum_price = sell_tickets * BOHEMIAN_RHAPSODY_ULTRA_LUXURY
elif (name_move == "Green Book") and (type_hall == "normal"):
    sum_price = sell_tickets * GREEN_BOOK_NORMAL
elif (name_move == "Green Book") and (type_hall == "luxury"):
    sum_price = sell_tickets * GREEN_BOOK_LUXURY
elif (name_move == "Green Book") and (type_hall == "ultra luxury"):
    sum_price = sell_tickets * GREEN_BOOK_ULTRA_LUXURY
elif (name_move == "The Favourite") and (type_hall == "normal"):
    sum_price = sell_tickets * THE_FAVOURITE_NORMAL
elif (name_move == "The Favourite") and (type_hall == "luxury"):
    sum_price = sell_tickets * THE_FAVOURITE_LUXURY
elif (name_move == "The Favourite") and (type_hall == "ultra luxury"):
    sum_price = sell_tickets * THE_FAVOURITE_ULTRA_LUXURY

print(f"{name_move} -> {sum_price:.2f} lv.")