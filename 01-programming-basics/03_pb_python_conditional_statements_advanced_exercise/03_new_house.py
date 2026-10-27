ROUSE = 5
DAHLIA = 3.80
TULIP = 2.80
NARCISSUS = 3
GLADIOLUS = 2.50

rose_discount = 0.1
dahlia_discount = 0.15
tulip_discount = 0.15
narcissus_surcharge = 0.15
gladiolus_surcharge = 0.20

type_flower = input()
count_flower = int(input())
budget = int(input())

price_flowers = 0

if type_flower == "Roses":
    price_flowers = ROUSE * count_flower
    if count_flower > 80:
        price_flowers -= price_flowers * rose_discount
if type_flower == "Dahlias":
    price_flowers = DAHLIA * count_flower
    if count_flower > 90:
        price_flowers -= price_flowers * dahlia_discount
if type_flower == "Tulips":
    price_flowers = TULIP * count_flower
    if count_flower > 80:
        price_flowers -= price_flowers * tulip_discount
if type_flower == "Narcissus":
    price_flowers = NARCISSUS * count_flower
    if count_flower < 120:
        price_flowers += price_flowers * narcissus_surcharge
if type_flower == "Gladiolus":
    price_flowers = GLADIOLUS * count_flower
    if count_flower < 80:
        price_flowers += price_flowers * gladiolus_surcharge

result = budget - price_flowers
if result >= 0:
    print(f"Hey, you have a great garden with {count_flower} {type_flower} and {abs(result):.2f} leva left.")
else:
    print(f"Not enough money, you need {abs(result):.2f} leva more.")