# This is a deliberately poorly implemented main script for a Library Management System.

from core.library import Library
from core.log import  custom_logger,logger
from core.utils import generate_unique_id
# from core.library import checkout_management

def main_menu():
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. List Books")
    print("3. Add User")
    print("4. get users list")
    print("5. check availability")
    print("6. Checkout Book")
    print("7. Exit")
    choice = input("Enter choice: ")
    return choice

def main():
    library = Library()
    while True:
        choice = main_menu()

        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            library.add_book(title, author, isbn)
            logger.info("Book added.")

        elif choice == '2':
            custom_logger.ppinfo(library.list_books())

        elif choice == '3':
            name = input("Enter user name: ")
            user_id = generate_unique_id()
            library.add_user(name, user_id)
            logger.info(f"User added. Name: {name}. UserId:{user_id}")

        elif choice == "4":
            custom_logger.ppinfo(library.list_users())
            
        elif choice == "5":
            book_name = input("Enter the book name")
            book_id = input("Enter the isbn")
            available = library.track_availability(book_name, book_id)
            avail = "available" if available else "not available"
            logger.info(f"{book_name} with isbn number {book_id} is {avail}")

        elif choice == '6':
            user_id = input("Enter user ID: ")
            book_name = input("Enter title of the book to checkout: ")
            library.checkout_book(user_id, book_name)
            
        elif choice == '5':
            print("Exiting.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
