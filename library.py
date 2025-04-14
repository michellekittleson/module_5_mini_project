from book import Book
from user import User
from author import Author
from connect_mysql import connect_database

# conn = connect_database()
# if conn is not None:
#     try:
#         cursor = conn.cursor()

#         query = "SELECT "
#     finally:
#         conn.close()

class Library:

    def __init__(self, name):
        self.books = []
        self.borrowed_books = []
        self.authors = []
        self.users = []

    def get_books(self):
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()
                query = "SELECT * from Books"
                cursor.execute(query)
                for row in cursor.fetchall():
                    print(row)

            finally:
                cursor.close()
                conn.close() 
        # if self.books:
        #     return self.books
        # else:
        #     return "No books in library"
        
    # Book Operations: 1. Add a New Book
    def add_book(self, title, author, isbn, publication_date): 
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()
                # new_book = Book(title, author, isbn, publication_date)
                query = "INSERT INTO Books (title, author_id, isbn, publication_date) VALUES (%s, %s, %s, %s)"
                cursor.execute(query, (title, author, isbn, publication_date))
                conn.commit()
            finally:
                cursor.close()
                conn.close()
        # self.books.append(new_book)
    

    def borrow_book(self, book, user): 
        if book in self.books: # Check for book in book list
            if book.availability: # check if book is available and rent out
                book.availability = False
                user.borrow_book(book)
                return f"Borrowed book '{book.title}'."
            else:
                return "Book is not available"
        else:
            return "Book not found in library"
    
    def return_book(self, book, user): 
        if book in self.books:
            if book.availability:
                return "Book has already been returned to the library."
            else:
                book.availability = True
                user.return_book(book)
                return f"Book '{book.title}' has been returned."
        else:
            return "Book not found."

    def search_title(self, title):
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor(buffered=True)
                query = "SELECT * from Books where title = %s"
                cursor.execute(query, (title,))
                book = cursor.fetchone()
                # conn.commit()
                print(f"Book: {book[1]}, ID: {book[0]}, ISBN: {book[3]}, Publication Date: {book[4]}")
            finally:
                cursor.close()
                conn.close()
    
    def get_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def add_user(self, name, library_id):
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()
                query = "INSERT INTO Users (name, library_id) VALUES (%s, %s)"
                cursor.execute(query, (name, library_id))
                conn.commit()
            finally:
                cursor.close()
                conn.close()
    
    def get_user(self, name):
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor(buffered=True)
                query = "SELECT * from Users where name = %s"
                cursor.execute(query, (name,))
                user = cursor.fetchone()
                # conn.commit()
                print(f"User: {user[1]}, ID: {user[0]}, Library ID: {user[2]}")
            finally:
                cursor.close()
                conn.close()
        # for user in self.users:
        #     if name == user.get_name():
        #         print("Found user")
        #         return user
        # print("No user found")    
        # return None # Return None if user not found
    
    def view_author_details(self, name):
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor(buffered=True)
                query = "SELECT * from Authors where name = %s"
                cursor.execute(query, (name,))
                author = cursor.fetchone()
                # conn.commit()
                print(f"Author: {author[1]}, ID: {author[0]}, Biography: {author[2]}")
            finally:
                cursor.close()
                conn.close()
    
    def get_users(self):
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()
                query = "SELECT * from Users"
                cursor.execute(query)
                for row in cursor.fetchall():
                    print(row)

            finally:
                cursor.close()
                conn.close()
        # for user in self.users:
        #     print(f"User name: {user.name}, Library ID: {user.get_library_id()}")
    
    def display_users(self):
        for user in self.users:
            print(user)
    
    def display_authors(self):
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()
                query = "SELECT * from Authors"
                cursor.execute(query)
                for row in cursor.fetchall():
                    print(row)

            finally:
                cursor.close()
                conn.close()
        # for author in self.authors:
        #     # print(author)
        #     print(f"Name: {author.name}, Biography: {author.biography}")
        # return True
    
    def add_author(self, name, biography):
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()
                new_author = Author(name, biography)
                query = "INSERT INTO authors (name, biography) VALUES (%s, %s)"
                cursor.execute(query, (name, biography))
                conn.commit()
            finally:
                cursor.close()
                conn.close()
    
    def find_author(self, name):
        for author in self.authors:
            print("type of author", type(author))
            print(author)
            if author.name == name:
                return author
        return None