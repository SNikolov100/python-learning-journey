from string import punctuation
punct = set(punctuation)
my_result = {}
with open("words.txt") as key_words:
    keys = set(key_words.read().split())

with open("input.txt") as source_file:
    text = source_file.read().lower()

new_text = ("".join(" " if char in punct else char for char in text)).split()
for char in new_text:
    if char in keys:
        my_result[char] = my_result.get(char, 0) + 1
sorted_result = sorted(my_result.items(), key=lambda x: -x[1])
for data in sorted_result:
    print(f"{data[0]} - {data[1]}")
