class Book:
    def __init__(self, title, author, genre, publication_date):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_date = publication_date
        self.availability = True
 
    def borrow(self):
        # If available, set to not available, if not available, set to available
        if self.availability:
            self.availability = False
            return True
        return False
    
    def return_book(self):
        self.availability = True
        










