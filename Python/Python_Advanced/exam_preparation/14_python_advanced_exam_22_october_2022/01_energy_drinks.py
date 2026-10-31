from collections import deque
MAX_CAFFEINE = 300
REDUCE_CAFFEINE = 30
caffeine_counter = 0
milligrams_of_caffeine = [int(cf) for cf in input().split(", ")]
energy_drinks = deque(int(ed) for ed in input().split(", "))

while milligrams_of_caffeine and energy_drinks:
    last_caffeine = milligrams_of_caffeine.pop()
    first_drink = energy_drinks.popleft()
    current_caffeine = last_caffeine * first_drink
    if (current_caffeine + caffeine_counter) <= MAX_CAFFEINE:
        caffeine_counter += current_caffeine
        if caffeine_counter > 300:
            caffeine_counter = 300
    else:
        energy_drinks.append(first_drink)
        caffeine_counter -= REDUCE_CAFFEINE
        caffeine_counter = max(0, caffeine_counter)

if energy_drinks:
    print(f"Drinks left: {', '.join(str(ed) for ed in energy_drinks)}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {caffeine_counter} mg caffeine.")

