name_product = input()
type_of_product = ""

if name_product in ("banana", "apple", "kiwi", "cherry", "lemon", "grapes"):
    type_of_product = "fruit"
elif name_product in ("tomato", "cucumber", "pepper", "carrot"):
    type_of_product = "vegetable"
else:
    type_of_product = "unknown"

print(type_of_product)
