def squares(n: int):
    # for num in range(1, n + 1):
    #     yield num * num
    yield from (num * num for num in range(1, n + 1))

print(list(squares(5)))