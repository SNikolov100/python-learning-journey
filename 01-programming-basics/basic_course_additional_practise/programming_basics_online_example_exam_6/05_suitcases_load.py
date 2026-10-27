capacity_airplane = float(input())
counter_3 = 0
is_Full = False
capacity_bag = 0

while True:
    volume_bag = input()

    if volume_bag == "End":
        break
    volume_bag_float = float(volume_bag)
    counter_3 += 1
    capacity_bag += volume_bag_float
    if counter_3 % 3 == 0:
        capacity_bag += volume_bag_float * 0.1

    if capacity_airplane < capacity_bag:
        counter_3 -= 1
        is_Full = True
        break

if is_Full:
    print(f"No more space!")
else:
    print(f"Congratulations! All suitcases are loaded!")
print(f"Statistic: {counter_3} suitcases loaded.")
