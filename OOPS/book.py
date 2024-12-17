class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"

class Library:
    def __init__(self, name):
        self.name = name  # City Library
        self.books = []  # List of books (aggregation)

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            print(book)

# Aggregation
library = Library("City Library")
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

library.add_book(book1)
library.add_book(book2)

library.show_books()
