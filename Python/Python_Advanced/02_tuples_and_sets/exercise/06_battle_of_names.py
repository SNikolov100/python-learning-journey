even_set = set()
odd_set = set()
for row in range(1, int(input())+1):
    temp_result = sum(ord(char) for char in input()) // row
    if temp_result % 2 == 0:
        even_set.add(temp_result)
    else:
        odd_set.add(temp_result)

if sum(even_set) == sum(odd_set):
    print(", ".join(str(x) for x in even_set.union(odd_set)))
elif sum(even_set) > sum(odd_set):
    print(", ".join(str(x) for x in even_set ^ odd_set))
else:
    print(", ".join(str(x) for x in odd_set - even_set))