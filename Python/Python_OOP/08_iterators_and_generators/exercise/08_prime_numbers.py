def get_primes(numbers:list[int]):
    for data in numbers:
        if data > 1:
            for num in range(2, data):
                if data % num == 0:
                    break
            else:
                yield data


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print(list(get_primes([-2, 0, 0, 1, 1, 0])))
