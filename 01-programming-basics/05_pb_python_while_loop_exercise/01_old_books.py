particular_book = input()

current_book = input()
is_find_book = False
count_books = 0

while current_book != particular_book:

    if current_book == "No More Books":
        is_find_book = True
        break

    current_book = input()
    count_books += 1


if is_find_book:
    print(f"The book you search is not here!\nYou checked {count_books} books.")
else:
    print(f"You checked {count_books} books and found it.")
