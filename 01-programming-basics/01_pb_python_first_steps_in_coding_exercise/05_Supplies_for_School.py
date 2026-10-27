PACK_PEN = 5.80
PACK_MARKER = 7.20
A_CLEANER = 1.20

number_pack_pens = int(input())
number_pack_markers = int(input())
liters_cleaner = int(input())
percent_discount = int(input()) / 100

price_pens = PACK_PEN * number_pack_pens
price_markers= PACK_MARKER * number_pack_markers
price_cleaner = A_CLEANER * liters_cleaner
all_result = price_pens + price_markers + price_cleaner
all_result -= all_result * percent_discount

print(all_result)