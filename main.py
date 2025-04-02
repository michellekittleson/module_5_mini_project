from book import Book
from library import Library
from author import Author


def main():

    my_library = Library("The Library")

    author = Author("Paulo Coelho", "Paulo Coelho is a Brazilian author who has published many books.")
    # Add defaults
    my_library.add_author(author)
    my_library.add_user("Alice", "1234")
    my_library.add_user("Bob", "5678")
    my_library.add_book("The Alchemist", "Paulo Coelho", "Fiction", 1988)


    while True:
        print("Welcome to the Library Management System!")
        print("\nMain Menu:\n1. Book Operations\n2. User Operations\n3. Author Operations\n4. Quit")

        choice = input("Enter your choice: ")
        
        try:
            if choice == '1':
                print("\nBook Operations:\n1. Add a new book\n2. Borrow a book\n3. Return a book\n4. Search for a book\n5. Display all books")
                choice = input("Enter your choice: ")
                try:

                    if choice == '1':
                        title = input("Enter title: ")
                        author = input("Enter author ID: ")
                        # genre = input("Enter genre: ")
                        publication_date = input("Enter publication date: ")
                        # my_library.add_book(title, author, genre, publication_date)
                        print(f"Book '{title}' has been added!")
                        
                    elif choice == '2':
                        title = input("Enter book to borrow: ").strip().title()

                        current_user = my_library.get_user(input("Enter user's name: "))

                        book = my_library.get_book(title)

                        print("calling book function")
                        borrowed_book_result = my_library.borrow_book(book, current_user)
                        print(borrowed_book_result)

                    elif choice == '3':
                        title = input("Enter book to return: ").strip().title()
                        current_user = my_library.get_user(input("Enter user's name: "))
                        book = my_library.get_book(title)
                        returned_book_result = my_library.return_book(book, current_user)
                        print(returned_book_result)

                    elif choice == '4':
                        title = input("Enter title to search: ")
                        if my_library.search_title(title):
                            print(f"Book '{title}' found.")
                        else:
                            print(f"Book '{title}' not found in the library.")

                    elif choice == '5':
                        library_books = my_library.get_books()
                        for book in library_books:
                            print(f"Title: {book.title}, Author: {book.author}, Genre: {book.genre}, Publication Date: {book.publication_date}")

                except Exception as e:
                    print(f"An error occurred: {e}")

            elif choice == '2':
                print("\nUser Operations:\n1. Add a new user\n2. View user details\n3. Display all users")
                choice = input("Enter your choice: ")
                try:

                    if choice == '1':
                        name = input("Enter user name: ")
                        library_id = input("Enter library id: ") 
                        my_library.add_user(name, library_id)

                    elif choice == '2':
                        name = input("Enter user name: ")
                        user = my_library.get_user(name) # Retrieve user object
                        if user:
                            print(user.name)
                        else:
                            print("User not found.")

                    elif choice == '3':
                        my_library.get_users()

                except Exception as e:
                    print(f"An error occurred: {e}")

            elif choice == '3':
                print("\nAuthor Operations:\n1. Add a new author\n2. View author details\n3. Display all authors")
                choice = input("Enter your choice: ")
                try:
                    # Create a new author 
                    if choice == '1':
                        name = input("Enter author name: ")
                        biography = input("Enter biography: ")
                        new_author = Author(name, biography)
                        my_library.add_author(new_author)
                        print(f"Author {name} has been added!")

                    elif choice == '2':
                        name = input("Enter author's name to search: ")
                        author = my_library.find_author(name)
                        print(author.view_author_details())

                    elif choice == '3':
                        all_authors = my_library.display_authors()

                except Exception as e:
                    print(f"An error occurred: {e}")

            elif choice == '4':
                print("Quitting system.")
                break
            
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()