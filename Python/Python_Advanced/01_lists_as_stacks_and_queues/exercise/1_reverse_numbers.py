entered_number = input().split()

for _ in range(len(entered_number)):
    print(entered_number.pop(), end=" ")
