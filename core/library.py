from datetime import datetime
from .books import Book
from .user import User
from store.storage import Storage
from .log import logger



class Library:
    def __init__(self):
        self.storage = Storage()

    def add_book(self, title:str, author:str, isbn:str):
        time_added = datetime.now()
        book = Book(title,author,isbn,time_added)
        book_data = book.get_data()
        self.storage.write_books(book_data)
        logger.info(f"{datetime.now()}: Added book {book.title}")

    def update_book(self, isbn: str, new_title: str = None, new_author: str = None):
        if not isinstance(isbn, str):
            raise ValueError("ISBN must be a string")
        if new_title is not None and not isinstance(new_title, str):
            raise ValueError("New title must be a string")
        if new_author is not None and not isinstance(new_author, str):
            raise ValueError("New author must be a string")
        
        for book in self.__books:
            if book.isbn == isbn:
                if new_title:
                    book.title = new_title
                if new_author:
                    book.author = new_author
                self.__logs.append(f"{datetime.datetime.now()}: Updated book {book.title}")
                print(f"Book '{book.title}' updated.")
                return
        print("Book not found.")

    def delete_book(self, isbn: str):
        if not isinstance(isbn, str):
            raise ValueError("ISBN must be a string")
        
        self.__books = [book for book in self.__books if book.isbn != isbn]
        self.__logs.append(f"{datetime.datetime.now()}: Deleted book with ISBN {isbn}")
        print(f"Book with ISBN '{isbn}' deleted.")

    def list_books(self):
        return self.storage.read_books()

    def search_books(self, title: str = None, author: str = None, isbn: str = None) -> list:
        if title is not None and not isinstance(title, str):
            raise ValueError("Title must be a string")
        if author is not None and not isinstance(author, str):
            raise ValueError("Author must be a string")
        if isbn is not None and not isinstance(isbn, str):
            raise ValueError("ISBN must be a string")

        results = [book for book in self.__books if
                   (title and book.title == title) or
                   (author and book.author == author) or
                   (isbn and book.isbn == isbn)]
        return results

    def add_user(self, user_name:str, user_id:str):
        user = User(user_name, user_id)
        if not isinstance(user, User):
            raise ValueError("Can only add instances of User")
        data = user.get_data()
        self.storage.write_users(data)
        logger.info(f"{datetime.now()}: Added user {user.name}")
        print(f"User '{user.name}' added.")

    def update_user(self, user_id: str, new_name: str = None):
        if not isinstance(user_id, str):
            raise ValueError("User ID must be a string")
        if new_name is not None and not isinstance(new_name, str):
            raise ValueError("New name must be a string")
        
        for user in self.__users:
            if user.user_id == user_id:
                if new_name:
                    user.name = new_name
                self.__logs.append(f"{datetime.datetime.now()}: Updated user {user.name}")
                print(f"User '{user.name}' updated.")
                return
        print("User not found.")

    def delete_user(self, user_id: str):
        if not isinstance(user_id, str):
            raise ValueError("User ID must be a string")
        
        self.__users = [user for user in self.__users if user.user_id != user_id]
        self.__logs.append(f"{datetime.datetime.now()}: Deleted user with ID {user_id}")
        print(f"User with ID '{user_id}' deleted.")

    def list_users(self):
        return self.storage.read_users()

    def search_users(self, name: str = None, user_id: str = None) -> list:
        if name is not None and not isinstance(name, str):
            raise ValueError("Name must be a string")
        if user_id is not None and not isinstance(user_id, str):
            raise ValueError("User ID must be a string")
        
        results = [user for user in self.__users if
                   (name and user.name == name) or
                   (user_id and user.user_id == user_id)]
        return results

    def checkout_book(self, user_id: str, book_name: str):
        

        if not self.storage.check_user(user_id):
            logger.error(f"User with id {user_id} does not exist")
            return 

        if not self.storage.check_availability(book_name):
            logger.error(f"{book_name} not available")
            return 
        
            
        done = self.storage.book_checkout(book_name)

        if done:
            self.storage.user_book_checkout(user_id,book_name)
            logger.info(f"Book {book_name} checked out to user {user_id}.")

    def check_in_book(self, user_id: str, isbn: str):
        if not isinstance(user_id, str):
            raise ValueError("User ID must be a string")
        if not isinstance(isbn, str):
            raise ValueError("ISBN must be a string")
        
        user = next((user for user in self.__users if user.user_id == user_id), None)
        book = next((book for book in self.__books if book.isbn == isbn), None)

        if not user:
            print("User not found.")
            return

        if not book:
            print("Book not found.")
            return

        if book not in user.borrowed_books:
            print(f"Book '{book.title}' was not borrowed by user '{user.name}'.")
            return

        book.check_in()
        user.return_book(book)
        self.__logs.append(f"{datetime.datetime.now()}: User {user.name} checked in book {book.title}")
        print(f"Book '{book.title}' checked in by user '{user.name}'.")

    def track_availability(self,book_name: str, isbn: str) -> str:
        return self.storage.check_availability(book_name)
    

    def show_logs(self):
        for log in self.__logs:
            print(log)
