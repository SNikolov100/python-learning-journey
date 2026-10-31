from collections import deque

green_light = int(input())
free_window = int(input())
cars_queue = deque()
is_crash  = False
passed_total_car = 0

while True:
    temp_green_light = green_light
    line = input()
    if line == "END" or is_crash:
        break
    if line == "green":

        while cars_queue:
            car = cars_queue.popleft()
            length_car = len(car)
            if length_car < temp_green_light:
                temp_green_light -= length_car
                passed_total_car += 1
            else:
                safe_time_to_move = temp_green_light + free_window
                if safe_time_to_move < length_car:
                    print(f"A crash happened!")
                    print(f"{car} was hit at {car[safe_time_to_move]}.")
                    is_crash = True
                else:
                    passed_total_car += 1
                break

    else:
        cars_queue.append(line)
if not is_crash:
    print(f"Everyone is safe.")
    print(f"{passed_total_car} total cars passed the crossroads.")
