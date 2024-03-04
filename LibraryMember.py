#Program to calculate library member
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
    
    def display_info(self):
        print(f"Book ID: {self.book_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        

class LibraryMember:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []
        
    def borrow_book(self, book):
        if isinstance(book, Book):
            self.borrowed_books.append(book)
        else:
            print("Invalid input. Please provide a Book name.")
    
    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
        else:
            print("The book is not currently borrowed by this member.")
    
    def display_info(self):
        print(f"Member ID: {self.member_id}")
        print(f"Name: {self.name}")
        print("Borrowed Books:")
        for book in self.borrowed_books:
            book.display_info()
            print()  # New line between each book entry

# Test the classes
book1 = Book(1, "Python Programming", "John Parker")
book2 = Book(2, "Data Structures", "Jane Smith")

member1 = LibraryMember(BSCIT-05-0209/2022, "Karen")
member1.borrow_book(book1)
member1.borrow_book(book2)

member1.display_info()
