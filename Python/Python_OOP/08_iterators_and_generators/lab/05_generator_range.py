def genrange(start: int, end: int):
    yield from (num for num in range(start, end + 1))

print(list(genrange(1, 10)))