import json
from typing import List, Dict, Any
import os
from core.books import Book

class Storage:
    def __init__(self, book_file: str = r"store\books.json", user_file: str = r"store\users.json"):
        self.book_file = book_file
        self.user_file = user_file
        self._initialize_files()

    def _initialize_files(self):
        # Initialize JSON files if they don't exist
        if not os.path.exists(self.book_file):
            with open(self.book_file, 'w') as f:
                json.dump([], f)
        if not os.path.exists(self.user_file):
            with open(self.user_file, 'w') as f:
                json.dump([], f)

    def read_books(self) -> List[Dict[str, Any]]:
        with open(self.book_file, 'r') as f:
            return json.load(f)

    def write_books(self, book: List[Dict[str, Any]]):
        with open(self.book_file,"r") as fp:
            data = json.load(fp)
        data.append(book)
        with open(self.book_file, 'w') as f:
            json.dump(data, f, indent=4)

    def read_users(self) -> List[Dict[str, Any]]:
        with open(self.user_file, 'r') as f:
            return json.load(f)

    def write_users(self, users: List[Dict[str, Any]]):
        with open(self.user_file,"r") as fp:
            data = json.load(fp)
        data.append(users)
        with open(self.user_file, 'w') as f:
            json.dump(data, f, indent=4)
    
    def check_availability(self,book_name:str):
        with open(self.book_file,"r") as fp:
            data = json.load(fp)
        available = next((True for book in data if book["_Book__title"] == book_name and book["_Book__is_checked_out"] == False), False)
        return available
    
    def check_user(self,user_id: str):
        with open(self.user_file,"r") as fp:
            data = json.load(fp)
        available = next((True for book in data if book["_User__user_id"] == user_id), False)
        return available
    
    def book_checkout(self,book_name:str):
        with open(self.book_file,"r") as fp:
            data = json.load(fp)
        for i in data:
            if i["_Book__title"] == book_name:
                i["_Book__is_checked_out"] = True
                break
        with open(self.book_file, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    
    def user_book_checkout(self,user_id: str,book_name:str):
        with open(self.user_file,"r") as fp:
            data = json.load(fp)
        for i in data:
            if i["_User__user_id"] == user_id:
                i["_User__borrowed_books"].append(book_name)
                break
        with open(self.user_file, 'w') as f:
            json.dump(data, f, indent=4)
    
                
        
