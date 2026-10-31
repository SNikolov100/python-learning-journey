from collections import deque
queue_name = deque()
quantity_water = int(input())

while True:
    command = input()
    queue_name.append(command)
    if command == "Start":
        break

while True:
    command = input()
    if command == "End":
        break
    if command.isdigit():
        if quantity_water >= int(command):
            quantity_water -= int(command)
            print(f"{queue_name.popleft()} got water")
        else:
            print(f"{queue_name.popleft()} must wait" )
    else:
        command_list = command.split()
        quantity_water += int(command_list[1])

print(f"{quantity_water} liters left")
