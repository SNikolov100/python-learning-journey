from collections import deque
bee_group = deque(map(int, input().split()))
bee_eater = [int(x) for x in input().split()]

while bee_group and bee_eater:
    defender = bee_group[0]
    attacker = bee_eater[-1]
    round_fight = defender // 7
    if round_fight < attacker:
        attacker -= round_fight
        bee_eater.pop()
        bee_group.popleft()
        bee_eater.append(attacker)

    elif round_fight > attacker:
        bee_eater.pop()
        round_fight = defender - attacker * 7
        bee_group.popleft()
        bee_group.append(round_fight)

    elif (round_fight == attacker) and (defender % 7 == 0):
        bee_eater.pop()
        bee_group.popleft()


    elif (round_fight == attacker) and (defender % 7 != 0):
        bee_eater.pop()
        bee_group.popleft()
        bee_group.append(defender - round_fight * 7)

print("The final battle is over!")
if not bee_eater and not bee_group:
    print(f"But no one made it out alive!")

if not bee_eater and bee_group:
    print(f"Bee groups left: {', '.join(str(x) for x in bee_group)}")

if not bee_group and bee_eater:
    print(f"Bee-eater groups left: {', '.join(str(x) for x in bee_eater)}")



