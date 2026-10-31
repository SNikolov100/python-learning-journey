import os

base_dir = os.path.dirname(os.path.abspath(__file__))
output_file_path = os.path.join(base_dir, "report.txt")
my_result = {}

for element in os.listdir(base_dir):
    file_path = os.path.join(base_dir, element)
    if os.path.isfile(file_path):
        ext = os.path.splitext(element)[-1]
        if ext not in  my_result:
            my_result[ext] = []
        my_result[ext].append(element)

with open(output_file_path, "w", encoding="utf-8") as file:
    for data in sorted(my_result):
        file.write(data + "\n")
        for name in sorted(my_result[data]):
            file.write(f"- - - {name}\n")

