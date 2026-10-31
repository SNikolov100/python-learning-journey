pile_clothes = list(map(int, input().split()))
capacity_rack = int(input())
rack = 0

while pile_clothes:
    rack += 1
    current_capacity = int(capacity_rack)
    while current_capacity != 0 and pile_clothes:
        if pile_clothes[-1] > current_capacity:
            break
        current_capacity -= pile_clothes[-1]
        pile_clothes.pop()


print(rack)