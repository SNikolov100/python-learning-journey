animal = input()
type_animal = ""

if animal == "dog":
    type_animal = "mammal"
elif (animal == "crocodile") \
        or (animal == "tortoise") \
        or (animal == "snake"):
    type_animal = "reptile"
else:
    type_animal = "unknown"

print(type_animal)
