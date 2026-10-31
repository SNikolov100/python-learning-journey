def plant_garden(space, *args, **kwargs):
    sorted_kwargs = sorted(kwargs.items(), key=lambda x: x[0])
    sorted_plants_dict = {}
    args_dict = {}
    not_enough_space = False
    my_result = []
    planted_plants = {}
    space = space * 100
    for plant, numbers in sorted_kwargs:
        sorted_plants_dict[plant] = numbers
    for plant, quality in args:
        args_dict[plant] = quality*100
    for plant, numbers in sorted_plants_dict.items():
        if plant in args_dict:
            for _ in range(1, numbers + 1):
                if space >= args_dict[plant]:
                    space -= args_dict[plant]
                    sorted_plants_dict[plant] -= 1
                    planted_plants[plant] = planted_plants.get(plant, 0) + 1
                else:
                    break
    for plant, number in sorted_plants_dict.items():
        if plant in args_dict:
            if sorted_plants_dict[plant] != 0:
                not_enough_space = True

    if not_enough_space:
        my_result.append(f"Not enough space to plant all requested plants!")
    else:
        my_result.append(f"All plants were planted! Available garden space: {space/100:.1f} sq meters.")
    my_result.append(f"Planted plants:")
    sorted_planted_plants = sorted(planted_plants.items(), key=lambda x: x[0])
    for plant, number in sorted_planted_plants:
        my_result.append(f"{plant}: {number}")
    return '\n'.join(my_result)













print(plant_garden(50.0, ("rose", 2.5), ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20))
print("==============================================")
print(plant_garden(20.0, ("rose", 2.0), ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20, sunflower=5))
print("=============================================")
print(plant_garden(2.0, ("rose", 2.5), ("tulip", 1.2), ("daisy", 0.2), rose=4, tulip=15, sunflower=3, daisy=4))
print("==============================================")
print(plant_garden(50.0, ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20, daisy=1))
