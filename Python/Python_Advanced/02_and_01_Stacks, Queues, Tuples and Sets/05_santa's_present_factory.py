from collections import deque

toys = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}

result = {}

materials = list(int(x) for x in input().split())
magic = deque(int(x) for x in input().split())

while materials and magic:
    product = materials[-1] * magic[0]
    if product in toys:
        create_toy = toys[(materials.pop() * magic.popleft())]
        if create_toy not in result:
            result[create_toy] = 0
        result[create_toy] += 1
    elif product < 0:
        materials.append(materials.pop() + magic.popleft())
    elif product > 0:
        magic.popleft()
        materials[-1] += 15
    else:
        if materials[-1] == 0:
            materials.pop()
        if magic[0] == 0:
            magic.popleft()

if ("Doll" in result and "Wooden train" in result) or ("Teddy bear" in result and "Bicycle" in result):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:
    print(f"Materials left: {', '.join(str(x) for x in reversed(materials))}")
if magic:
    print(f"Magic left: {', '.join(str(i) for i in magic)}")

for toy, number in sorted(result.items()):
    print(f"{toy}: {number}")

