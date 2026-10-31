from math import floor
from sys import maxsize
max_word = ""
sum_max_word = - maxsize

sum_word = 0
while True:
    word = input()
    if word == "End of words":
        break
    length = len(word)
    sum_one_word = 0
    for index in range(length):
        temp_first_char = word[0]
        temp_char = word[index]
        if temp_first_char in ("a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y"):
            sum_one_word += ord(temp_char) * length
        else:
            sum_one_word += floor(ord(temp_char) / length)

    if sum_max_word < sum_one_word:
        sum_max_word = sum_one_word
        max_word = word

print(f"The most powerful word is {max_word} - {sum_max_word}")

