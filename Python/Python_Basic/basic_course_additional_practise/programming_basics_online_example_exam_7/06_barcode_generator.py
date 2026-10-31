start = int(input())
end = int(input())

start_str = str(start)
end_str = str(end)
s1 = int(start_str[0])
s2 = int(start_str[1])
s3 = int(start_str[2])
s4 = int(start_str[3])
e1 = int(end_str[0])
e2 = int(end_str[1])
e3 = int(end_str[2])
e4 = int(end_str[3])
is_Even = True

for index_1 in range(s1, e1 +1):
    for index_2 in range(s2, e2 + 1):
        for index_3 in range(s3, e3 + 1):
            for index_4 in range(s4, e4 + 1):
                if (index_1 % 2 == 0) or (index_2 % 2 == 0) or (index_3 % 2 == 0) or (index_4 % 2 == 0):
                    is_Even = True
                else:
                    print(f"{index_1}{index_2}{index_3}{index_4}", end=" ")







