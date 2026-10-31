from collections import deque

packages = [int(x) for x in input().split()]
couriers = deque(int(x) for x in input().split())
total_weight = 0

while packages and couriers:
    package = packages[-1]
    courier = couriers.popleft()
    if courier >= package:
        if courier > package:
            courier -= package * 2
            if courier > 0:
                couriers.append(courier)
        total_weight += package
        packages.pop()
    else:
        packages[-1] -= courier
        total_weight += courier

print(f"Total weight: {total_weight} kg")
if not packages and not couriers:
    print("Congratulations, all packages were delivered successfully by the couriers today.")
elif packages and not couriers:
    print(f"Unfortunately, there are no more available couriers to deliver the following packages:"
          f" {', '.join(str(pack) for pack in packages)}")
elif couriers and not packages:
    print(f"Couriers are still on duty: "
          f"{', '.join(str(cour) for cour in couriers)} but there are no more packages to deliver.")




