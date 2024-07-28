from datetime import datetime

# Global list to store books
books = []


class Book():
    def __init__(self,title:str,author:str,isbn:str,date_added:datetime) -> None:
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__is_checked_out = False
        self.__due_date = None
        self.__date_added = datetime.strftime(date_added,"%d:%m:%y")
    
    @property
    def title(self)->str:
        return self.__title
    
    @title.setter
    def title(self,value:str):
        if not isinstance(value, str):
            raise ValueError("title must be a string")
        self.__title = value
    
    @property
    def author(self)->str:
        return self.__author
    
    @author.setter
    def author(self,value:str):
        if not isinstance(value, str):
            raise ValueError("author must be a string")
        self.__author = value
    

    @property
    def isbn(self) -> str:
        return self.__isbn

    @isbn.setter
    def isbn(self, value: str):
        if not isinstance(value, str):
            raise ValueError("ISBN must be a string")
        self.__isbn = value
    

    @property
    def due_date(self) -> datetime:
        return self.__due_date
    
    def get_data(self) -> dict:
        return self.__dict__

    def check_out(self):
        self.__is_checked_out = True
        self.__due_date = datetime.datetime.now() + datetime.timedelta(days=14)

    def check_in(self):
        self.__is_checked_out = False
        self.__due_date = None

    def __repr__(self):
        return f"Book(title={self.__title}, author={self.__author}, isbn={self.__isbn}, checked_out={self.__is_checked_out})"


 

def add_book(title, author, isbn):

    
    books.append({"title": title, "author": author, "isbn": isbn})

def list_books():
    for book in books:
        print(book)

