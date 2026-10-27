import math, sys
PACK_SUGAR = 950
PACK_FLOUR = 750

number_easter_bread = int(input())
total_sugar = 0
total_flour = 0
max_sugar = - sys.maxsize
max_flour = - sys.maxsize

for _ in range(number_easter_bread):
    use_sugar = int(input())
    use_flour = int(input())
    total_sugar += use_sugar
    total_flour += use_flour
    if max_sugar < use_sugar:
        max_sugar = use_sugar

    if max_flour < use_flour:
        max_flour = use_flour

total_pack_sugar = math.ceil(total_sugar / PACK_SUGAR)
total_pack_floor = math.ceil(total_flour / PACK_FLOUR)

print(f"Sugar: {total_pack_sugar}")
print(f"Flour: {total_pack_floor}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")