def classify_books(*args, **kwargs):
    result = []
    fiction_books = {}
    no_fiction_books = {}

    for genre, book_title in args:
        for number, title in kwargs.items():
            if book_title == title:
                if genre == "fiction":
                    fiction_books[book_title] = number
                else:
                    no_fiction_books[book_title] = number
    sorted_fiction = sorted(fiction_books.items(), key=lambda x: x[1])
    sorted_no_fiction = sorted(no_fiction_books.items(), key=lambda x: x[1], reverse=True)
    if sorted_fiction:
        result.append("Fiction Books:")
        for book, number in sorted_fiction:
            result.append(f"~~~{number}#{book}")
    if sorted_no_fiction:
        result.append("Non-Fiction Books:")
        for book, number in sorted_no_fiction:
            result.append(f"***{number}#{book}")
    return '\n'.join(result)

print(classify_books(
    ("fiction", "Brave New World"),
    ("non_fiction", "The Art of War"),
    NF3421NN="The Art of War",
    FF1234UU="Brave New World"
))
print(classify_books(
    ("non_fiction", "The Art of War"),
    ("fiction", "The Great Gatsby"),
    ("non_fiction", "A Brief History of Time"),
    ("fiction", "Brave New World"),
    FF1234HH="The Great Gatsby",
    NF3845UU="A Brief History of Time",
    NF3421NN="The Art of War",
    FF1234UU="Brave New World"
))
print(classify_books(
    ("fiction", "Brave New World"),
    ("fiction", "The Catcher in the Rye"),
    ("fiction", "1984"),
    FICCITRZZ="The Catcher in the Rye",
    FIC1984XX="1984",
    FICBNWYYY="Brave New World"
))
print(classify_books(
    ("non_fiction", "Sapiens"),
    ("non_fiction", "Homo Deus"),
    ("non_fiction", "The Selfish Gene"),
    NF123ABC="Sapiens",
    NF987XYZ="Homo Deus",
    NF456DEF="The Selfish Gene"
))
