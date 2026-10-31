parking_lot = set()

for _ in range(int(input())):
    direction, car_number = input().split(", ")
    if direction == "IN":
        parking_lot.add(car_number)
    elif direction == "OUT" and car_number in parking_lot:
        parking_lot.remove(car_number)

if not parking_lot:
    print("Parking Lot is Empty")
else:
    for number in parking_lot:
        print(number)

