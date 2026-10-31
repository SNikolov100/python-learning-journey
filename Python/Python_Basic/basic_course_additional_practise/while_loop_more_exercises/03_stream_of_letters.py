flag_c = True
flag_o = True
flag_n = True

letters = ""
symbol = ""
print_letters = ""

while True:
    symbol = input()

    if symbol == "End":
        break

    if symbol.isalpha() and symbol.isascii():
        if symbol in ("c", "o", "n"):

            if symbol == "c" and flag_c:
                flag_c = False
            elif symbol == "o" and flag_o:
                flag_o = False
            elif symbol == "n" and flag_n:
                flag_n = False
            else:
                letters += symbol

            if not flag_c and not flag_o and not flag_n:
                flag_c = True
                flag_o = True
                flag_n = True
                letters += " "
                print_letters = letters

        else:
            letters += symbol

print(print_letters)









