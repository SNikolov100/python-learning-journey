def shop_from_grocery_list(budget, *args):
    result = []
    shopping_dict = {}
    grocery_list = args[0]
    for product_name, price in args[1:]:
        if product_name in grocery_list and product_name not in shopping_dict:
            budget -= price
            if budget < 0:
                break
            grocery_list.remove(product_name)
            shopping_dict[product_name] = price
    if not grocery_list:
        result.append(f"Shopping is successful. Remaining budget: {budget:.2f}.")
    else:
        result.append(f"You did not buy all the products. Missing products: {', '.join(grocery_list)}.")
    return '\n'.join(result)

print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))
print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))
print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))
