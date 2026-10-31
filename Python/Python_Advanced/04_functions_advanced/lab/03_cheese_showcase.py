def sorting_cheeses(**kwargs):
    new_data = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    result = ""
    for chees, pieces in new_data:
        result += f"{chees}\n"

        for piece in sorted(pieces, key=lambda x: -x):
            result += f"{piece}\n"
    return result






print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
print("=========================")

print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)

