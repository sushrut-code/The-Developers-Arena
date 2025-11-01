from book import Book
from member import Member
from library import Library


def main():
    """This function will run our main application loop."""
    my_library = Library()
    print("Welcome to the Library Management System!")

    while True:

        print("\n--- Main Menu ---")
        print("1. Add a new Book")
        print("2. Add a new Member")
        print("3. Lend a Book")
        print("4. Receive a Book")
        print("5. List all available Books")
        print("6. Exit")


        choice = input("Enter your choice (1-6): ")


        if choice == '1':

            print("\n--- Add New Book ---")

            book_title=input("Enter the book's title: ")
            book_author=input("Enter the book's author: ")
            book_isbn=input("Enter the book's ISBN: ")
            book_new=Book(book_title,book_author,book_isbn)
            my_library.add_book(book_new)


        elif choice == '2':

            print("\n--- Add New Member ---")
            # Your code here:
            member_name=input("Enter the name of the member: ")
            member_id=input("enter the member_id of the member: ")
            member_new=Member(member_name,member_id)
            my_library.add_member(member_new)


        elif choice == '3':

            print("\n--- Lend Book ---")
            # Your code here:
            book_title=input("Enter the book's title: ")
            member_id=input("Enter the member_id of the person to whom we will lend this book: ")
            my_library.lend_book(book_title,member_id)


        elif choice == '4':

            print("\n--- Receive Book ---")

            book_title = input("Enter the book's title: ")
            member_id = input("Enter the member_id of the person to whom we will lend this book: ")

            my_library.receive_book(book_title, member_id)


        elif choice == '5':
            print("\n--- Available Books ---")

            my_library.list_available_books()



        elif choice == '6':

            print("Thank you for using the Library System. Goodbye!")
            break  # This exits the while True loop

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")




main()