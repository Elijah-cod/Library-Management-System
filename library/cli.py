from .models import Author, Book

def main_menu():
    while True:
        print("\nLibrary Management System")
        print("1. Add Author")
        print("2. View All Authors")
        print("3. Delete Author")
        print("4. Add Book")
        print("5. View All Books")
        print("6. Delete Book")
        print("7. Find Book")
        print("8. Find Author")
        print("9. Exit")
        
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Author Name: ")
            birth_date = input("Birth Date (YYYY-MM-DD): ")
            nationality = input("Nationality: ")
            Author.create(name, birth_date, nationality)

        elif choice == "2":
            authors = Author.get_all()
            for author in authors:
                print(author)

        elif choice == "3":
            name = input("Enter Author Name to Delete: ")
            Author.delete(name)

        elif choice == "4":
            title = input("Book Title: ")
            genre = input("Genre: ")
            publication_date = input("Publication Date (YYYY-MM-DD): ")
            author_name = input("Author Name: ")
            Book.create(title, genre, publication_date, author_name)

        elif choice == "5":
            books = Book.get_all()
            for book in books:
                print(book)

        elif choice == "6":
            title = input("Enter Book Title to Delete: ")
            Book.delete(title)
        
        elif choice == "7":
            title = input("Enter Book Title to Find: ")
            print(Book.find_by_title(title))
            
        elif choice == "8":
            name = input("Enter Author Name to Find: ")
            print(Author.find_by_name(name))

        elif choice == "9":
            print("Exiting...")
            break

        else:
            print("Invalid option. Try again.")


# To allow the code to run only when the main menu is called
if __name__ == "__main__":
    main_menu()
