from collections import  deque

armor_monsters = deque([int(x) for x in input().split(",")])
soldier_striking = [int(x) for x in input().split(",")]
total_killed_monsters = 0

while armor_monsters and soldier_striking:
    value_monster = armor_monsters.popleft()
    value_soldier = soldier_striking.pop()
    impact = value_soldier - value_monster
    if impact == 0:
        total_killed_monsters += 1
    elif 0 < impact:
        total_killed_monsters += 1
        if soldier_striking:
            soldier_striking[-1] += impact
        else:
            soldier_striking.append(impact)
    elif impact < 0:
        armor_monsters.append(abs(impact))

if not armor_monsters:
    print("All monsters have been killed!")
if not soldier_striking:
    print("The soldier has been defeated.")
print(f"Total monsters killed: {total_killed_monsters}")