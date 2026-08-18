# Library Management System using OOP

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True


class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name


class Library:
    def __init__(self):
        self.books = [None] * 50
        self.patrons = [None] * 50
        self.book_count = 0
        self.patron_count = 0

    # Add Book
    def add_book(self, book):
        if self.book_count < 50:
            self.books[self.book_count] = book
            self.book_count = self.book_count + 1
            print("Book added successfully.")
        else:
            print("Library is full.")

    # Register Patron
    def register_patron(self, patron):
        if self.patron_count < 50:
            self.patrons[self.patron_count] = patron
            self.patron_count = self.patron_count + 1
            print("Patron registered successfully.")
        else:
            print("Patron limit reached.")

    # Borrow Book
    def borrow_book(self, book_id):
        i = 0
        while i < self.book_count:
            if self.books[i].book_id == book_id:
                if self.books[i].available == True:
                    self.books[i].available = False
                    print("Book borrowed successfully.")
                else:
                    print("Book is already borrowed.")
                return
            i = i + 1
        print("Book not found.")

    # Return Book
    def return_book(self, book_id):
        i = 0
        while i < self.book_count:
            if self.books[i].book_id == book_id:
                if self.books[i].available == False:
                    self.books[i].available = True
                    print("Book returned successfully.")
                else:
                    print("Book was not borrowed.")
                return
            i = i + 1
        print("Book not found.")

    # Display Books
    def display_books(self):
        print("\nLibrary Books:")
        i = 0
        while i < self.book_count:
            status = "Available"
            if self.books[i].available == False:
                status = "Borrowed"

            print("ID:", self.books[i].book_id)
            print("Title:", self.books[i].title)
            print("Author:", self.books[i].author)
            print("Status:", status)
            print("---------------------")
            i = i + 1


# Main Program
library = Library()

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Register Patron")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Display Books")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book_id = int(input("Enter Book ID: "))
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        book = Book(book_id, title, author)
        library.add_book(book)

    elif choice == 2:
        patron_id = int(input("Enter Patron ID: "))
        name = input("Enter Patron Name: ")
        patron = Patron(patron_id, name)
        library.register_patron(patron)

    elif choice == 3:
        book_id = int(input("Enter Book ID to Borrow: "))
        library.borrow_book(book_id)

    elif choice == 4:
        book_id = int(input("Enter Book ID to Return: "))
        library.return_book(book_id)

    elif choice == 5:
        library.display_books()

    elif choice == 6:
        print("Exiting...")
        break

    else:
        print("Invalid choice.")
