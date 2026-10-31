def shopping_cart(*args):
    result = []
    max_soup = 3
    max_pizza = 4
    max_dessert = 2
    meal_dict = {
        "Soup": [],
        "Pizza": [],
        "Dessert": []
        }
    has_product = False

    for data in args:
        if data == "Stop":
            break
        meal_type, product_meal = data
        if len(meal_dict["Soup"]) == max_soup and meal_type == "Soup":
            continue
        if len(meal_dict["Pizza"]) == max_pizza and meal_type == "Pizza":
            continue
        if len(meal_dict["Dessert"]) == max_dessert and meal_type == "Dessert":
            continue
        if product_meal in meal_dict[meal_type]:
            continue
        meal_dict[meal_type].append(product_meal)
        has_product = True
    if not has_product:
        return f"No products in the cart!"
    sorted_meal = sorted(meal_dict.items(), key=lambda x: (-len(x[1]), x[0]))

    for meal_type, products in sorted_meal:
        result.append(f"{meal_type}:")
        for product in sorted(products):
            result.append(f" - {product}")
    return '\n'.join(result)





print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))
print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
