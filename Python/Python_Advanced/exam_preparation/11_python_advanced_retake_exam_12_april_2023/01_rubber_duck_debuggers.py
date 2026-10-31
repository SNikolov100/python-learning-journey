from collections import deque

duck_dictionary = {
        "Darth Vader Ducky": 0,
        "Thor Ducky": 0,
        "Big Blue Rubber Ducky": 0,
        "Small Yellow Rubber Ducky": 0
    }
intervals = ((0, 60, "Darth Vader Ducky"),
             (61, 120, "Thor Ducky"),
             (121, 180, "Big Blue Rubber Ducky"),
             (181, 240, "Small Yellow Rubber Ducky")
            )

time_to_complete_task = deque(int(x) for x in input().split())
number_of_tasks = [int(x) for x in input().split()]

while time_to_complete_task and number_of_tasks:

    time = time_to_complete_task.popleft()
    number = number_of_tasks.pop()
    multiply = time * number
    max_number = intervals[-1][1]
    if multiply > max_number:
        number -= 2
        number_of_tasks.append(number)
        time_to_complete_task.append(time)

    for lo, hi, name in intervals:
        if lo <= multiply <= hi:
            duck_dictionary[name] += 1

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")

print(f"Darth Vader Ducky: {duck_dictionary['Darth Vader Ducky']}")
print(f"Thor Ducky: {duck_dictionary['Thor Ducky']}")
print(f"Big Blue Rubber Ducky: {duck_dictionary['Big Blue Rubber Ducky']}")
print(f"Small Yellow Rubber Ducky: {duck_dictionary['Small Yellow Rubber Ducky']}")