from project.user import User


class Library:
    def __init__(self):
        self.user_records:list[User] = []
        self.books_available:dict = {}
        self.rented_books: dict = {}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        if author in self.books_available and book_name in self.books_available[author]:
            if not user.username in self.rented_books:
                self.rented_books[user.username] = {}
            self.rented_books[user.username][book_name] = days_to_return
            self.books_available[author].remove(book_name)
            user.books.append(book_name)
            return f"{book_name} successfully rented for the next {days_to_return} days!"
        for username, data in self.rented_books.items():
            for bookname, days_left in data.items():
                if bookname == book_name:
                    return f'The book "{book_name}" is already rented and will be available in {days_left} days!'

    def return_book(self, author:str, book_name:str, user: User):
        if user.username in self.rented_books:
            if book_name in self.rented_books[user.username]:
                self.rented_books[user.username].pop(book_name)
                user.books.remove(book_name)
                if author not in self.books_available:
                    self.books_available[author] = []
                self.books_available[author].append(book_name)
                return
        return f"{user.username} doesn't have this book in his/her records!"


