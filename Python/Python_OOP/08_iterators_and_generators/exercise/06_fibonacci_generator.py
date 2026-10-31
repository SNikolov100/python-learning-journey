def fibonacci():
    first_num = 0
    second_num = 1
    while True:
        result = first_num + second_num
        yield first_num
        first_num, second_num = result, first_num


generator = fibonacci()
for i in range(5):
    print(next(generator))
generator = fibonacci()
for i in range(1):
    print(next(generator))
