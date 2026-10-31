def reverse_text(data):
    # yield from (data[ch] for ch in range(len(data)-1, -1, -1))
    # for ch in reversed(data):
    #     yield ch
    yield from reversed(data)

for char in reverse_text("step"):
    print(char, end='')
