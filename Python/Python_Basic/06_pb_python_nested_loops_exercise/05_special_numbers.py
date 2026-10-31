current_number = int(input())
magic_number = 0

for var_number in range(1111, 10000):
    is_magic = True
    for value in str(var_number):
        if int(value) == 0:
            is_magic = False
            break
        else:
            if current_number % int(value) != 0:
                is_magic = False
                break
    if is_magic:
        print(var_number, end=" ")




