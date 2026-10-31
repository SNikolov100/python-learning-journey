from collections import deque

pumps = int(input())
info_pumps = deque()
start_position = 0
stop = 0

for _ in range(pumps):
    command = input().split()
    petrol, distance = int(command[0]), int(command[1])
    info_pumps.append({'Fuel': int(petrol), 'Capacity': int(distance)})

while stop < pumps:
    stop += 1
    petrol, distance = 0, 0
    for i in range(pumps):
        petrol += info_pumps[i]['Fuel']
        distance = info_pumps[i]['Capacity']
        if petrol < distance:
            info_pumps.rotate(-1)
            stop = 0
            start_position += 1
            break
        petrol -= distance

print(start_position)

