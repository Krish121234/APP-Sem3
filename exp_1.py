class Book:
    def __init__(self, name, author, genre):
        self.name = name
        self.author = author
        self.genre = genre


class Patreon:
    def __init__(self, patreon_id, name, borrowed_books=None):
        self.patreon_id = patreon_id
        self.name = name
        self.borrowed_books = [] if borrowed_books is None else borrowed_books

    def display(self):
        print(f"Patreon id: {self.patreon_id}")
        print(f"Patreon name: {self.name}")
        print("Borrowed Books:")
        if not self.borrowed_books:
            print("- None")
        else:
            for book in self.borrowed_books:
                print(f"- {book.name}")


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added {book.name} to the library.")

    def register_patreon(self, patreon):
        self.patrons.append(patreon)
        print(f"Registered {patreon.name}.")

    def borrow(self, patreon, book):
        if book in self.books:
            if book not in patreon.borrowed_books:
                patreon.borrowed_books.append(book)
                print(f"{patreon.name} borrowed {book.name}")
            else:
                print(f"{patreon.name} already borrowed {book.name}")
        else:
            print(f"{book.name} is not in the library.")

    def return_(self, patreon, book):
        if book in patreon.borrowed_books:
            patreon.borrowed_books.remove(book)
            print(f"{patreon.name} returned {book.name}")
        else:
            print(f"{patreon.name} does not have {book.name}")


# Example usage
book1 = Book("White Nights", "Fyodor Dostoevsky", "Fiction")
book2 = Book("Shadow Slave", "Guiltythree", "Webnovel")

alice = Patreon(101, "Alice")
library = Library()

library.add_book(book1)
library.add_book(book2)
library.register_patreon(alice)
library.borrow(alice, book1)
alice.display()
library.return_(alice, book1)
alice.display()

