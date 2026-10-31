from math import ceil

EASTER_BREAD = 4
EGG = 0.45

number_guest = int(input())
budget = float(input())

sum_easter_bread = ceil(number_guest / 3)
sum_eggs = number_guest * 2
price_easter_bread = sum_easter_bread * EASTER_BREAD
price_eggs = sum_eggs * EGG
price_total = price_eggs + price_easter_bread
diff = abs(budget - price_total)
if budget >= price_total:
     print(f"Lyubo bought {sum_easter_bread} Easter bread and {sum_eggs} eggs.")
     print(f"He has {diff:.2f} lv. left.")
else:
    print(f"Lyubo doesn't have enough money.")
    print(f"He needs {diff:.2f} lv. more.")
