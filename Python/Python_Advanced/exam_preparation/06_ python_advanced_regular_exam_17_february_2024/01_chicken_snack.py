from collections import deque

amount_of_money = [int(x) for x in input().split()]
prices_of_foods = deque(int(x) for x in input().split())
count_foods = 0

while amount_of_money and prices_of_foods:
    money = amount_of_money.pop()
    food = prices_of_foods.popleft()
    if money == food:
        count_foods += 1
        continue
    if money > food:
        money -= food
        if amount_of_money:
            amount_of_money[-1] += money
        count_foods += 1

if count_foods >= 4:
    print(f"Gluttony of the day! Henry ate {count_foods} foods.")
elif count_foods == 0:
    print("Henry remained hungry. He will try next weekend again.")
elif count_foods == 1:
    print(f"Henry ate: {count_foods} food.")
else:
    print(f"Henry ate: {count_foods} foods.")

