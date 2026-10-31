a1 = int(input())
a2 = int(input())
n = int(input())

for count_1 in range(a1, a2):
    if count_1 % 2 != 0:
        symbol_1 = chr(count_1)
        for count_2 in range(1, n):
            symbol_2 = count_2
            end_3 = (n // 2)
            for count_3 in range(1, end_3):
                symbol_3 = count_3
                symbol_4 = ord(symbol_1)
                temp_check = symbol_2 + symbol_3 + symbol_4
                if temp_check % 2 != 0:
                    print(f"{symbol_1}-{symbol_2}{symbol_3}{symbol_4}")






