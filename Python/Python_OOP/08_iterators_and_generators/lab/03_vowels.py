class vowels:
    vowel_chars = {"a", "e", "i", "u", "y", "o"}
    def __init__(self, data: str):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.data):
            ch = self.data[self.index]
            self.index += 1
            if ch.lower() in self.vowel_chars:
                return ch
        raise StopIteration

my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
