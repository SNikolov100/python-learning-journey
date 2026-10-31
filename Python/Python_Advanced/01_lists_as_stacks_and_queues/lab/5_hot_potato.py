from collections import deque

name_deque = deque(input().split())
toss = int(input())

while True:
    if len(name_deque) <=1:
        break
    for _ in range(toss-1):
        name_deque.rotate(-1)
    print(f"Removed {name_deque.popleft()}")

print(f"Last is {name_deque.popleft()}")
