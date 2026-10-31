# from collections import deque


# class dictionary_iter:
#     def __init__(self, data_dictionary: dict):
#         self.data_dictionary = deque(data_dictionary.items())
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if not self.data_dictionary:
#             raise StopIteration
#         return self.data_dictionary.popleft()
class dictionary_iter:
    def __init__(self, data_dictionary: dict):
        self.data_dictionary = iter(data_dictionary.items())

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.data_dictionary)

result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
