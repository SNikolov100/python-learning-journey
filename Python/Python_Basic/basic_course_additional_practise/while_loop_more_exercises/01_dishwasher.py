BOTTLE = 750
FOR_ONE_DISHES = 5
FOR_ONE_POT = 15

count_bottles = int(input())
count_dishes_pot = 0
is_End = True
amount_detergent = count_bottles * BOTTLE
variable_detergent = 0
enter_count = 0
clean_dishes = 0
clean_pot = 0


while amount_detergent >= 0:
    enter_data = input()
    enter_count += 1

    if enter_data == "End":
        is_End = False
        break
    else:
        count_dishes_pot = int(enter_data)

    if enter_count % 3 == 0:
        amount_detergent -= count_dishes_pot * FOR_ONE_POT
        clean_pot += count_dishes_pot
    else:
        amount_detergent -= count_dishes_pot * FOR_ONE_DISHES
        clean_dishes += count_dishes_pot

if amount_detergent >= 0:
    print(f"Detergent was enough!")
    print(f"{clean_dishes} dishes and {clean_pot} pots were washed.")
    print(f"Leftover detergent {amount_detergent} ml.")
else:
    print(f"Not enough detergent, {abs(amount_detergent)} ml. more necessary!")

