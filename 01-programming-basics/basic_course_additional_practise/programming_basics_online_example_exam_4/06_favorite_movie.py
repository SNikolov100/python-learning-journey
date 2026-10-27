from sys import maxsize
max_reit = - maxsize
char_to_int = 0
best_movie = ""
is_End = True

for _ in range(7):
    temp_reiting = 0
    name_movie = input()
    if name_movie == "STOP":
        is_End = False
        break
    len_name_movie = len(name_movie)

    for char in range(len_name_movie):
        one_char = name_movie[char]
        char_to_int = ord(one_char)
        if 65 <= char_to_int <= 90:
            temp_reiting += (char_to_int - len_name_movie)
        elif 97 <= char_to_int <= 122:
            temp_reiting += (char_to_int - (2 * len_name_movie))
        else:
            temp_reiting += char_to_int

    if max_reit < temp_reiting:
        max_reit = temp_reiting
        best_movie = name_movie

if is_End:
    print(f"The limit is reached.")
print(f"The best movie for you is {best_movie} with {max_reit} ASCII sum.")


