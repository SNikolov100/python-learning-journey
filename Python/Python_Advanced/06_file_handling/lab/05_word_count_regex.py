import re

pattern = r"\b[a-z0-9]+"
my_result = {}

with open("words.txt") as key_words_file, open("input.txt") as input_file:
    keys_text = set(key_words_file.read().lower().split())
    input_text = input_file.read()

input_words = re.findall(pattern, input_text, re.IGNORECASE)
for word in input_words:
    word = word.lower()
    if word in keys_text:
        my_result[word] = my_result.get(word, 0) + 1

sorted_result = sorted(my_result.items(), key=lambda x: -x[1] )
for data in sorted_result:
    print(f"{data[0]} - {data[1]}")

