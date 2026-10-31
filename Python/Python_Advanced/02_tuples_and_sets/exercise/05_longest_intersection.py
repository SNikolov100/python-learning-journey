def create_set(range_area: str) -> set:
    start, end = map(int, range_area.split(","))
    return set(x for x in range(start, end + 1))

result = []
max_element = 0
for _ in range(int(input())):
    first, second = input().split("-")
    set_one = create_set(first)
    set_two = create_set(second)
    result_sets = set_one & set_two
    if max_element < len(result_sets):
        max_element = len(result_sets)
        result = result_sets

if result:
    print(f"Longest intersection is [{', '.join(str(x) for x in result)}] with length {len(result)}")