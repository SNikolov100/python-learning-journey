def accommodate_new_pets(capacity:int,weight_limit:float, *args ):
    not_capacity = False
    result = []
    accommodate_dict = {}
    for pet_type, pet_weight in args:
        if capacity == 0:
            not_capacity = True
            break
        if pet_weight > weight_limit:
            continue
        if pet_type not in accommodate_dict:
            accommodate_dict[pet_type] = []
        accommodate_dict[pet_type].append(pet_weight)

        capacity -= 1
    if not_capacity:
         result.append("You did not manage to accommodate all pets!")
    elif capacity >= 0:
        result.append(f"All pets are accommodated! Available capacity: {capacity}.")


    sorted_accommodate_pets = sorted(accommodate_dict.items(), key=lambda x: x[0])
    result.append("Accommodated pets:")
    for type_pet, count_pets in sorted_accommodate_pets:
        result.append(f"{type_pet}: {len(count_pets)}")
    return '\n'.join(result)


print(accommodate_new_pets(
    10,
    15.0,
    ("cat", 5.8),
    ("dog", 10.0),
))
print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))
print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))
