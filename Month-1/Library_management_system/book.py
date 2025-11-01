class Book:
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.is_checked_out=False

    def check_out(self):
        self.is_checked_out=True

    def return_book(self):
        self.is_checked_out=False





