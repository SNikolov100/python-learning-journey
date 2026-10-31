def recursive_power(x, y):
    if y == 1:
        return x
    return x * recursive_power(x, y-1)


print(recursive_power(2, 10))

print(recursive_power(10, 100))

