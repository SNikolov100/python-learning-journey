import os
from string import punctuation

base_dir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(base_dir, "text.txt")
output_file = os.path.join(base_dir, "output.txt")

if os.path.exists(input_file) and os.path.isfile(input_file):
    with open(input_file, encoding="utf-8") as open_file, open(output_file, "w", encoding="utf-8") as write_file:
        content = open_file.read().splitlines()
        for index, line in enumerate(content):
            count_letter = sum(1 if ch.isalpha() else 0 for ch in line)
            count_punct = sum(1 if ch in punctuation else 0 for ch in line)
            result = f"Line {index + 1}: {line} ({count_letter})({count_punct})"
            write_file.write(result + "\n")
