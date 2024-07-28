from datetime import datetime
from .books import Book
from .user import User
from store.storage import Storage
from .log import logger



class Library:
    def __init__(self):
        self.__storage = Storage()

    def add_book(self, title:str, author:str, isbn:str):
        time_added = datetime.now()
        book = Book(title,author,isbn,time_added)
        book_data = book.get_data()
        self.__storage.write_books(book_data)
        logger.info(f"{datetime.now()}: Added book {book.title}")

    def update_book(self, isbn: str, checkout_status: str):
        status = self.__storage.update_book_status(isbn, checkout_status)
        if status:
            return True
        logger.info("Book Update Error.")
        return False
    

    def delete_book(self, book_name: str, isbn:str):
        status = self.__storage.delete_book(book_name,isbn)
        logger.info(f"Book with ISBN '{isbn}' deleted.")
        return status

    def list_books(self):
        return self.__storage.read_books()
    
    def track_availability(self,book_name: str) -> bool:
        return self.__storage.check_availability(book_name)

    def search_books(self, title: str = None, author: str = None, isbn: str = None) :
        availability, book = self.__storage.check_availability(title, return_data=True)
        
        return book

    def add_user(self, user_name:str, user_id:str):
        user = User(user_name, user_id)
        if not isinstance(user, User):
            raise ValueError("Can only add instances of User")
        data = user.get_data()
        self.__storage.write_users(data)
        logger.info(f"{datetime.now()}: Added user {user.name}")
        logger.info(f"User '{user.name}' added.")
        return True

    def update_user(self, user_id: str, new_name: str = None):
        status = self.__storage.update_user(user_id, new_name)
        if status:
            logger.info(f"User {user_id} updated")
            return True
        logger.info("User not found.")

    def delete_user(self, user_id: str):
        status = self.__storage.delete_user(user_id)
        logger.info(f"User with ID '{user_id}' deleted.")
        return True

    def list_users(self):
        return self.__storage.read_users()

    def search_users(self,user_id: str = None):
        available, data = self.__storage.check_user(user_id, return_data=True)
        
        return data

    def checkout_book(self, user_id: str, book_name: str):
        

        if not self.__storage.check_user(user_id):
            logger.error(f"User with id {user_id} does not exist")
            return 

        if not self.__storage.check_availability(book_name):
            logger.error(f"{book_name} not available")
            return 
        
            
        done = self.__storage.book_checkout(book_name) #checking the availability of book updating status of it if True 

        if done:
            self.__storage.user_book_checkout(user_id,book_name)
            logger.info(f"Book {book_name} checked out to user {user_id}.")
        return done

    def checkin_book(self, user_id: str, book_name: str):
        
        available, user_data = self.__storage.check_user(user_id,return_data=True)
        if available and book_name not in user_data["_User__borrowed_books"]:
            logger.info("Wrong book checkin")
            return False
        self.__storage.user_book_checkin(user_id,book_name)
        return True
        
        
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

    

    def show_logs(self):
        for log in self.__logs:
            print(log)
