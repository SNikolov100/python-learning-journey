from collections import deque
quantities_food = int(input())
queue_orders = deque(map(int, input().split()))

print(max(queue_orders))

for _ in range(len(queue_orders)):
    if queue_orders[0] <= quantities_food:
        quantities_food -= queue_orders.popleft()
    else:
        break

if queue_orders:
    print(f"Orders left: ", end="")
    for _ in range(len(queue_orders)):
        print(f"{queue_orders.popleft()}", end=" ")
else:
    print("Orders complete")
