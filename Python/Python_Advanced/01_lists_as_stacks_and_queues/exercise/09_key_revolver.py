from collections import deque

price_of_each_bullet = int(input())
size_of_the_gun_barrel = int(input())
bullets = [int(x) for x in input().split()]
locks = deque(int(x) for x in input().split())
value_money = int(input())
counter_bullets = 0

while bullets and locks:
    current_bullet = bullets.pop()
    current_lock = locks[0]
    counter_bullets += 1
    value_money -= price_of_each_bullet
    if current_bullet <= current_lock:
        print("Bang!")
        locks.popleft()
    else:
        print("Ping!")

    if counter_bullets == size_of_the_gun_barrel:
        if bullets:
            print("Reloading!")
            counter_bullets = 0

if not locks:
    print(f"{len(bullets)} bullets left. Earned ${value_money}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")