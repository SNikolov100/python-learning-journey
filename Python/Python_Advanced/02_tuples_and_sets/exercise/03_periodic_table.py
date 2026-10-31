chemical_comp = set()

for _ in range(int(input())):
    chemical_comp.update(input().split())

print(*chemical_comp, sep="\n")

