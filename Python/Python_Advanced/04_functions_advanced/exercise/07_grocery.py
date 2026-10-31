def grocery_store(**kwargs):
    sorted_grocery = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

    result = []
    for product_name, product_quantity in sorted_grocery:
        result.append(f"{product_name}: {product_quantity}")
    return "\n".join(result)





print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
print("======================")
print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))

