my_result = []
entered_data = input().split("|")
for index in range(len(entered_data)-1,-1,-1):
    data = entered_data[index].split()
    if data:
        my_result.extend(data)

print(' '.join(my_result))

