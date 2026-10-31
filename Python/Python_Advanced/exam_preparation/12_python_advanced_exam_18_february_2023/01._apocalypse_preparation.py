from collections import deque

result = {
    "Patch": 0,
    "Bandage": 0,
    "MedKit": 0
}
create_healing_item = (("Patch", 30), ("Bandage", 40), ("MedKit", 100))
textiles = deque(int(x) for x in input().split())
medicaments = [int(x) for x in input().split()]

while textiles and medicaments:
    is_create_potion = False
    first_textile = textiles.popleft()
    last_medic = medicaments.pop()
    sum_materials = first_textile + last_medic
    greater_healing_item, max_resource = create_healing_item[-1]
    if sum_materials > max_resource:
        result[greater_healing_item] += 1
        if medicaments:
            medicaments[-1] += (sum_materials - max_resource)
        else:
            medicaments.append(sum_materials - max_resource)
        continue
    for healing_item, resource in create_healing_item:
        if sum_materials == resource:
            result[healing_item] += 1
            is_create_potion = True
            break
    if not is_create_potion:
        last_medic += 10
        medicaments.append(last_medic)

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not medicaments:
    print("Medicaments are empty.")

sorted_result = sorted(result.items(), key=lambda x: (-x[1], x[0]))
for item_name, amount_created in sorted_result:
    if amount_created > 0:
        print(f"{item_name} - {amount_created}")

if medicaments:
    medicaments.reverse()
    print(f"Medicaments left: {', '.join(str(m) for m in medicaments)}")
elif textiles:
    print(f"Textiles left: {', '.join(str(t) for t in textiles)}")

