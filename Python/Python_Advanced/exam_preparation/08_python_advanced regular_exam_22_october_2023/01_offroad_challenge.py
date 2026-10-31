from collections import deque

fuel = [int(x) for x in input().split()]
consumption_index = deque(int(x) for x in input().split())
quantities = deque(int(x) for x in input().split())
altitude_counter = 0
is_not_reach = False
result_altitude = []

while fuel and consumption_index:
    last_fuel = fuel[-1]
    first_consumption = consumption_index[0]
    first_quantity = quantities[0]
    result = last_fuel - first_consumption
    altitude_counter += 1
    if result >= first_quantity:
        fuel.pop()
        consumption_index.popleft()
        quantities.popleft()
        print(f"John has reached: Altitude {altitude_counter}")
        result_altitude.append(f"Altitude {altitude_counter}")
    else:
        print(f"John did not reach: Altitude {altitude_counter}")
        is_not_reach = True
        break

if is_not_reach and result_altitude:
    print("John failed to reach the top.")
    print(f"Reached altitudes: {', '.join(x for x in result_altitude)}")

if is_not_reach and not result_altitude:
    print("John failed to reach the top.")
    print("John didn't reach any altitude.")

if not is_not_reach:
    print("John has reached all the altitudes and managed to reach the top!")