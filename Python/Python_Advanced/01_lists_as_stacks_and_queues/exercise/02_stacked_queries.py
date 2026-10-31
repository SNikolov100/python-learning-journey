query_stack = []
count_query = int(input())

for _ in range(count_query):
    command = input().split()
    if command[0] == "1":
        query_stack.append(int(command[1]))
    elif command[0] == "2":
        if query_stack:
            query_stack.pop()
    elif command[0] == "3" and query_stack:
        print(max(query_stack))
    elif command[0] == "4" and query_stack:
        print(min(query_stack))

if query_stack:
    for _ in range(len(query_stack)-1):
        print(query_stack.pop(), end=", ")
    print(query_stack.pop())

