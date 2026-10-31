parentheses_dict = {
    "}": "{",
    ")": "(",
    "]": "["
}

entered_data = input()
temp_storage = []

for char in entered_data:
    if not temp_storage:
        temp_storage.append(char)
        continue
    if char not in parentheses_dict:
        temp_storage.append(char)
        continue
    else:
        if parentheses_dict[char] == temp_storage[-1]:
            temp_storage.pop()

if temp_storage:
    print("NO")
else:
    print("YES")



