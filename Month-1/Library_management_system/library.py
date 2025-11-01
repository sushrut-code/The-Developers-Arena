from book import Book
from member import Member

class Library:

    def __init__(self):
        self.catalog={}
        self.members={}

    def list_available_books(self):
        print(self.catalog.keys())

    def add_book(self, book):
        self.catalog[book.title]=book


    def add_member(self, member):
        self.members[member.member_id]=member

    def lend_book(self, book_title, member_id):
        # This is the most complex method. Read the steps!


        book = self.catalog.get(book_title)
        member = self.members.get(member_id)

        # 3. --- Start checking for errors ---
        if book is None or member is None:
            print("Error: Book or Member not found")
            return

        if book.is_checked_out:
            print("Error: Book is already checked out.")
            return

        book.check_out()
        member.borrow_book(book)
        print(f"Successfully lent '{book_title}' to {member.name}.")


    def receive_book(self, book_title, member_id):
        # This is the reverse of lend_book

        # 1. Find the book object
        book = self.catalog.get(book_title)

        # 2. Find the member object
        member = self.members.get(member_id)

        if book is None or member is None:
            print("Error: Book or Member not found")
            return

        if book not in member.borrowed_books:
            print("Error: Member does not have this book.")
            return

        book.return_book()
        member.return_book(book)
        print(f"Successfully received '{book_title}' from {member.name}.")
