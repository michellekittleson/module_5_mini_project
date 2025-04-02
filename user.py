class User:
    def __init__(self, name, library_id):
        self.name = name
        self.__library_id = library_id
        self.__borrowed_books = []
    
    def borrow_book(self, book):
        if book in self.__borrowed_books:
            return "Book already borrowed."
        # Borrow the book
        else:
            self.__borrowed_books.append(book)
            return f"Borrowed book '{book.title}'."
    
    def get_borrowed_books(self):
        return self.__borrowed_books
    
    def return_book(self, book):
        if book in self.__borrowed_books:
            book.availability = True
            self.__borrowed_books.remove(book)
        else:
            return False
    
    def view_user_details(self):
        return {
            "Name": self.name,
            "Biography": self.biography
        }
    
    def get_name(self):
        return self.name
    
    def get_library_id(self):
        return self.__library_id