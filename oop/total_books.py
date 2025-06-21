#Create a class Book with a class variable total_books to count the number of book instances created.
#Implement a class method display_total_books() to display the total number of books created.

class Books:
    total_books = 0
    def __init__(self, book):
        self.book = book
        Books.total_books += 1
        
    @classmethod
    def display_total_books(cls):
        return f"Total number of books available: {cls.total_books}"
    
    
book1 = Books('Book1')
book2 = Books('Book2')
print(Books.display_total_books())
