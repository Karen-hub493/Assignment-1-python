class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.borrowed = False

    def borrow_book(self):
        if not self.borrowed:
            self.borrowed = True
            print(f"The book '{self.title}' has been borrowed.")
        else:
            print(f"The book '{self.title}' is already borrowed.")

    def return_book(self):
        if self.borrowed:
            self.borrowed = False
            print(f"The book '{self.title}' has been returned.")
        else:
            print(f"The book '{self.title}' is not currently borrowed.")

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Publication Year: {self.publication_year}")
        print(f"Borrowed: {'Yes' if self.borrowed else 'No'}")


book1 = Book("Python programming", "John Parker", 1925)
book2 = Book("Telecommunications", "Karen cherop", 1960)

book1.display_info()

book1.borrow_book()
book1.display_info()

book1.return_book()
book1.display_info()
