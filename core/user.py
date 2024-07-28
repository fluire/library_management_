from .books import Book
users = []

class User:
    def __init__(self, name: str, user_id: str):
        self.name = name
        self.user_id = user_id
        self.__borrowed_books = []

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        self.__name = value

    @property
    def user_id(self) -> str:
        return self.__user_id

    @user_id.setter
    def user_id(self, value: str):
        if not isinstance(value, str):
            raise ValueError("User ID must be a string")
        self.__user_id = value

    @property
    def borrowed_books(self) -> list:
        return self.__borrowed_books
    
    def get_data(self):
        return self.__dict__

    def borrow_book(self, book: Book):
        if not isinstance(book, Book):
            raise ValueError("Can only borrow instances of Book")
        self.__borrowed_books.append(book)

    def return_book(self, book: Book):
        if not isinstance(book, Book):
            raise ValueError("Can only return instances of Book")
        self.__borrowed_books.remove(book)

    def __repr__(self):
        return f"User(name={self.__name}, user_id={self.__user_id}, borrowed_books={[book.title for book in self.__borrowed_books]})"

def add_user(name, user_id):
    users.append({"name": name, "user_id": user_id})
