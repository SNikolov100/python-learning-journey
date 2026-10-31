GOAL_STEPS = 10_000

count_steps = 0
result = ""
day_steps = 0
is_going_home = False

while count_steps < GOAL_STEPS:
    input_data = input()
    if input_data == "Going home":
        input_data = input()
        day_steps = int(input_data)
        count_steps += day_steps
        is_going_home = True
        break

    day_steps = int(input_data)
    count_steps += day_steps

if is_going_home and (count_steps < GOAL_STEPS):
    print(f"{GOAL_STEPS - count_steps} more steps to reach goal.")
else:
    print(f"Goal reached! Good job!\n{count_steps - GOAL_STEPS} steps over the goal!")





