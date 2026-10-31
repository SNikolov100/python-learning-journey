border_number = int(input())
sequence_number = 0

while True:
    sequence_number = (2 * sequence_number) + 1
    if border_number < sequence_number:
        break
    else:
        print(sequence_number)