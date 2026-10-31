from collections import deque

making_honey ={
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
}


working_bees = deque(int(i) for i in input().split())
nectar = [int(i) for i in input().split()]
actions = deque(input().split())
honey = 0

while working_bees and nectar:
    if nectar[-1] >= working_bees[0]:
        if actions[0] == "/" and nectar[-1] == 0:
            working_bees.popleft()
            nectar.pop()
            actions.popleft()
            continue
        honey += abs(making_honey[actions.popleft()](working_bees.popleft(), nectar.pop()))
    else:
        nectar.pop()

print(f"Total honey made: {honey}")

if working_bees:
    print(f"Bees left: {', '.join(str(i) for i in working_bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(i) for i in nectar)}")

