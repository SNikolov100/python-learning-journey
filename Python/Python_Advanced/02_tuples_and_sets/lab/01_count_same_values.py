occurrence_tuple = tuple(float(x) for x in input().split())
temp_data = []
for char in occurrence_tuple:
    if char in temp_data:
        continue
    temp_data.append(char)
    print(f"{char} - {occurrence_tuple.count(char)} times")
