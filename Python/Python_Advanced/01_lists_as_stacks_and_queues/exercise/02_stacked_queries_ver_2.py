lines = int(input())
query_stack = []

type_query = {
    "1": lambda x: query_stack.append(int(x)),
    "2": lambda : query_stack.pop() if query_stack else None,
    "3": lambda : print(max(query_stack)) if query_stack else None,
    "4": lambda : print(min(query_stack)) if query_stack else None,
}

for i in range(lines):
    command = input().split()
    type_query[command[0]](*command[1:])
query_stack.reverse()
print(*query_stack, sep= ', ')
