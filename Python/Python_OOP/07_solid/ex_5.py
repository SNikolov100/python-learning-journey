class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter:
    def format(self, book: Book) -> str:
        return book.content


class Printer:
    def get_book(self, book: Book, formatter: Formatter):
        formatted_book = formatter.format(book)
        return formatted_book

b1 = Book("Hello")
f1 = Formatter()
p1 = Printer()

print(p1.get_book(b1, f1))