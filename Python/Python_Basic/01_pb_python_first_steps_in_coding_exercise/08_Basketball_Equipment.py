annual_tax = int(input())

basket_shoes = annual_tax - annual_tax * 0.4
basket_equipment = basket_shoes - basket_shoes * 0.2
basket_ball = basket_equipment * 0.25
basket_accessories = basket_ball / 5

total_price = annual_tax + \
              basket_shoes + \
              basket_equipment + \
              basket_ball + \
              basket_accessories

print(total_price)