entered_text = input()
unique_char = set()

for char in entered_text:
    unique_char.add(char)

sorted_txt = sorted(unique_char)

for ch in sorted_txt:
    print(f"{ch}: {entered_text.count(ch)} time/s")




