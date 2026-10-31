from collections import deque

products = deque()
robots = input().split(";")
start_times = tuple(int(x) for x in input().split(":"))
robots_dict = {}
is_taken = False

for robot in robots:
    name, time = robot.split("-")
    robots_dict[name] = [int(time), 0]

while True:
    line = input()
    if line == "End":
        break
    products.append(line)
start_time_in_seconds = start_times[0]*3600 + start_times[1]*60 + start_times[2]
work_time = start_time_in_seconds

while products:
    work_time += 1
    is_taken = False
    for robot_name, time in robots_dict.items():
        if time[1] <= work_time:
            hours = work_time // 3600
            minutes = (work_time - hours*3600 )// 60
            seconds = work_time - hours*3600 - minutes*60
            print(f"{robot_name} - {products.popleft()} [{hours % 24:02d}:{minutes:02d}:{seconds:02d}]")
            time[1] = work_time + time[0]
            is_taken = True
            break

    if not is_taken:
        products.rotate(-1)


