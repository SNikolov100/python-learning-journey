from sys import maxsize

min_number = maxsize
break_point = True
number = 0
while break_point:
    import_data = input()
    if import_data == "Stop":
        break_point = False
    else:
        number = int(import_data)
    if number < min_number:
        min_number = number

print(min_number)
