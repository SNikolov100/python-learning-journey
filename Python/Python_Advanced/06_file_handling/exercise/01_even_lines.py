import os
my_result = []
replace_characters = {"-", ",", ".", ",", "!", "?"}
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "text.txt")

if os.path.exists(file_path) and os.path.isfile(file_path):
    with open(file_path) as file:
        content = file.read().split("\n")

for index, line in enumerate(content):
    if index % 2 == 0:
        line = "".join("@" if ch in replace_characters else ch for ch in line )
        print(' '.join(reversed(line.split())))



