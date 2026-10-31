from collections import deque

cup_capacity = deque(int(x) for x in input().split())
bottle_capacity = [int(x) for x in input().split()]
wasted_water = 0

while bottle_capacity and cup_capacity:
    bottle = bottle_capacity.pop()
    if bottle >= cup_capacity[0]:
        wasted_water += (bottle - cup_capacity.popleft())
    else:
        cup_capacity[0] -= bottle

if not cup_capacity:
    print(f"Bottles: {' '.join(map(str, bottle_capacity))}")
else:
    print(f"Cups: {' '.join(map(str, cup_capacity))}")

print(f"Wasted litters of water: {wasted_water}")
