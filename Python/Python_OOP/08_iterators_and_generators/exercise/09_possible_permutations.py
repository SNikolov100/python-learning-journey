from itertools import permutations


def possible_permutations(collection:list):
        for data in permutations(collection):
            data = list(data)
            yield data


[print(n) for n in possible_permutations([1, 2, 3])]
[print(n) for n in possible_permutations([1])]
