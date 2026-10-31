from collections import deque
temp_sequence = deque()
sequence = deque(x for x in input().split())

operators = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x // y,
}

for _ in range(len(sequence)):
    element = sequence.popleft()
    if element in ["*", "+", "-", "/"]:
        result = temp_sequence.popleft()
        if temp_sequence:
            for _ in range(len(temp_sequence)):
                temp_number = temp_sequence.popleft()
                result = operators[element](result, temp_number)
        temp_sequence.append(result)
    else:
        temp_sequence.append(int(element))

print(*temp_sequence)
