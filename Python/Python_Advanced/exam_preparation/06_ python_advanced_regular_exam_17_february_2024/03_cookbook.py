def cookbook(*args):
    my_recipes = {}
    for name_food, cuisine, ingredients in args:
        if not cuisine in my_recipes:
            my_recipes[cuisine] = {}
        my_recipes[cuisine][name_food] = ingredients
    result = []
    sorted_my_recipes = sorted(my_recipes.items(), key=lambda x: (-len(x[1]), x[0]))
    for cuisine, name_food in sorted_my_recipes:
        result.append(f"{cuisine} cuisine contains {len(name_food)} recipes:")
        sorted_to_name =sorted(name_food.items(), key=lambda x: x[0])
        for name, ingredient in sorted_to_name:
            result.append(f"  * {name} -> Ingredients: {', '.join(ingredient)}")
    return '\n'.join(result)





print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))
print("=============================================")
print(cookbook(
    ("Pad Thai", "Thai", ["rice noodles", "shrimp", "peanuts", "bean sprouts", "tamarind sauce"])
    ))
print("================================================")
print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
    ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
    ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
    ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
    ))
