expression = input()
stack_result = []
print_result = []

for index in range(len(expression)):
    if expression[index] == "(":
        stack_result.append(index)
    elif expression[index] == ")" and len(stack_result) > 0:
        start_index=stack_result.pop()
        end_index = index + 1
        print_result.append(expression[start_index:end_index])

for index in range(len(print_result)):
    print(print_result[index])