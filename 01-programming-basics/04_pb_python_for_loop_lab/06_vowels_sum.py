input_text = input()

sum_vowel_letters = 0

for char in input_text:
    if char == "a":
        sum_vowel_letters += 1
    elif char == "e":
        sum_vowel_letters += 2
    elif char == "i":
        sum_vowel_letters += 3
    elif char == "o":
        sum_vowel_letters += 4
    elif char == "u":
        sum_vowel_letters += 5

print(sum_vowel_letters)
