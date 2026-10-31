class reverse_iter:
    def __init__(self, data):
        self.data = data
        self.start = len(self.data)-1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < 0:
            raise StopIteration
        value = self.data[self.start]
        self.start -= 1
        return value

reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
