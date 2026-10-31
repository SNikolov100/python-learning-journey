CHICKEN_MENU = 10.35
FISH_MENU = 12.40
VEGAN_MENU = 8.15
DELIVERY = 2.50

number_chicken_menus = int(input())
number_fish_menus = int(input())
number_vegan_menus = int(input())

price_chicken = number_chicken_menus * CHICKEN_MENU
price_fish = number_fish_menus * FISH_MENU
price_vegan = number_vegan_menus * VEGAN_MENU
price_meal = price_chicken + price_fish + price_vegan
price_desert = price_meal * 0.2
price_end = DELIVERY + price_meal + price_desert

print(price_end)