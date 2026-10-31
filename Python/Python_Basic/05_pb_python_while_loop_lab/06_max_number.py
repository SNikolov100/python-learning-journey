import sys

max_number = - sys.maxsize

while True:
    input_data =(input())
    if input_data == "Stop":
        break
    else: input_number = int(input_data)
    if input_number > max_number:
        max_number = input_number

print(max_number)


