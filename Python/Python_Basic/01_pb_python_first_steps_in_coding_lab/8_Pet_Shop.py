number_of_packages_from_dogs = int(input())
number_of_packages_from_cats = int(input())

price_pack_dogs = 2.50
price_pack_cats = 4

final_amount_dogs = number_of_packages_from_dogs * price_pack_dogs
final_amount_cats = number_of_packages_from_cats * price_pack_cats
final_amount = final_amount_dogs + final_amount_cats
print(f"{final_amount} lv.")
