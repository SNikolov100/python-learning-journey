import os
base_dir = os.path.dirname(os.path.abspath(__file__))

while True:
    line = input()
    if line == "End":
        break
    command, file_name, *args = line.split("-")
    file_path = os.path.join(base_dir, file_name)
    if command == "Create":
        open(file_path, "w").close()
    elif command == "Add":
        with open(file_path, "a") as file:
            file.write(f"{args[0]}\n")
    elif command == "Replace":
        try:
            with open(file_path, "r") as file:
                content = file.read()
        except FileNotFoundError:
            print("An error occurred")
            continue
        content = content.replace(args[0], args[1])
        with open(file_path, "w") as file:
            file.write(content)
    elif command == "Delete":
        try:
            os.remove(file_path)
        except FileNotFoundError:
            print("An error occurred")

