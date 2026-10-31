
set_one = set(map(int, (input().split())))
set_two = set(map(int, (input().split())))

for _ in range(int(input())):
    command = input().split()
    word_key = command[0] + " " + command[1]
    numbers = list(map(int, command[2:]))
    if word_key == "Add First":
        set_one.update(numbers)
    elif word_key == "Add Second":
        set_two.update(numbers)
    elif word_key == "Remove First":
        set_one.difference_update(numbers)
    elif word_key == "Remove Second":
        set_two.difference_update(numbers)
    elif word_key == "Check Subset":
        print(set_one.issubset(set_two) or set_two.issubset(set_one))

print(f"{', '.join(str(x) for x in sorted(set_one))}")
print(f"{', '.join(str(x) for x in sorted(set_two))}")
