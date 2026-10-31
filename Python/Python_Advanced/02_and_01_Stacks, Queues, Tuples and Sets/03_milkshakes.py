from collections import deque

chocolates = [int(i) for i in input().split(", ")]
cup_of_milk = deque(int(i) for i in input().split(", "))
milkshakes = 0
while milkshakes < 5 and chocolates and cup_of_milk :
    if chocolates[-1] <= 0 and cup_of_milk[0] <= 0:
        chocolates.pop()
        cup_of_milk.popleft()
        continue
    if chocolates[-1] <= 0:
        chocolates.pop()
        continue
    if cup_of_milk[0] <= 0:
        cup_of_milk.popleft()
        continue
    if chocolates[-1] == cup_of_milk[0]:
        milkshakes += 1
        chocolates.pop()
        cup_of_milk.popleft()
        continue
    cup_of_milk.rotate(-1)
    chocolates[-1] -= 5
    if chocolates[-1] <= 0:
        chocolates.pop()

if milkshakes == 5:
    print(f"Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolates:
    print(f"Chocolate: {', '.join(str(i) for i in chocolates)}")
else:
    print("Chocolate: empty")
if cup_of_milk:
    print(f"Milk: {', '.join(str(i) for i in cup_of_milk)}")
else:
    print("Milk: empty")