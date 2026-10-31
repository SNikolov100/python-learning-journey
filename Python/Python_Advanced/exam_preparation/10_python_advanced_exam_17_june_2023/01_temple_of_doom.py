from collections import deque

tools = deque(int(x) for x in input().split())
substances = [int(x) for x in input().split()]
challenges = list(int(x) for x in input().split())

while tools and substances:
    tool = tools.popleft()
    substance = substances.pop()
    result = tool * substance
    if result in challenges:
        challenges.remove(result)
    else:
        tools.append(tool + 1)
        substance -= 1
        if substance > 0:
            substances.append(substance)

if challenges:
    print("Harry is lost in the temple. Oblivion awaits him.")
else:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")

if tools:
    print(f"Tools: {', '.join(str(tool) for tool in tools)}")
if substances:
    print(f"Substances: {', '.join(str(subs) for subs in substances)}")
if challenges:
    print(f"Challenges: {', '.join(str(chall) for chall in challenges)}")
