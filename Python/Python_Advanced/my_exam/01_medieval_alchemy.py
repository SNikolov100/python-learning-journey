from collections import deque

potion_lab = (
    ("Brew of Immortality", 110),
    ("Essence of Resilience", 100),
    ("Draught of Wisdom", 90),
    ("Potion of Agility", 80),
    ("Elixir of Strength", 70),
)

substances = [int(x) for x in input().split(", ")]
crystal_energy = deque(int(x) for x in input().split(", "))
crafted_potion = []

while substances and crystal_energy:
    first_crystal = crystal_energy.popleft()
    last_subs = substances.pop()
    sum_mix = first_crystal + last_subs
    is_equal = False
    for potion, level in potion_lab:
        if sum_mix == level:

            if potion not in crafted_potion:
                is_equal = True
                crafted_potion.append(potion)
                break
    if not is_equal:
        for potion, level in potion_lab:
            if sum_mix > level and potion not in crafted_potion:
                is_equal = True
                crafted_potion.append(potion)
                first_crystal -= 20
                if first_crystal > 0:
                    crystal_energy.append(first_crystal)
                break
    if not is_equal:
        first_crystal -= 5
        if first_crystal > 0:
            crystal_energy.append(first_crystal)
    if len(crafted_potion) == 5:
        break

if len(crafted_potion) == 5:
    print("Success! The alchemist has forged all potions!")
else:
    print("The alchemist failed to complete his quest.")
if crafted_potion:
    print(f"Crafted potions: {', '.join(str(p) for p in crafted_potion )}")
if substances:
    print(f"Substances: {', '.join(str(s) for s in reversed(substances))}")
if crystal_energy:
    print(f"Crystals: {', '.join(str(s) for s in crystal_energy)}")



