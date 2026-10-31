number_N = int(input())
number_M = int(input())
number_S = int(input())

for number in range(number_M, number_N-1, -1):
    if number % 2 == 0:
        if number % 3 == 0:
            if number == number_S:
                break
            print(number, end=" ")
