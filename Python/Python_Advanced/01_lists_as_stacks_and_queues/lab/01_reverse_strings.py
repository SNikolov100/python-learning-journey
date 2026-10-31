entered_string = list(input())
stack_string = []

#for _ in range(len(entered_string)):
#    print(entered_string.pop(), end="")

for _ in range(len(entered_string)):
    stack_string.append(entered_string.pop())

print("".join(stack_string))



