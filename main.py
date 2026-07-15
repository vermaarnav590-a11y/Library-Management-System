import os

class Book:

    def __init__(self, title, author, issued=False):
        self.title = title
        self.author = author
        self.issued = issued


books = []

if os.path.exists("books.txt"):

    with open("books.txt", "r") as file:

        for line in file:

            data = line.strip().split(",")

            if len(data) == 3:

                title = data[0]
                author = data[1]
                issued = data[2] == "True"

                books.append(Book(title, author, issued))

print("=" * 55)
print("        LIBRARY MANAGEMENT SYSTEM")
print("=" * 55)

while True:

    print("\nChoose an option:")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Delete Book")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ")

    
    if choice == "1":

        title = input("\nEnter Book Title: ").strip().title()

        author = input("Enter Author Name: ").strip().title()

        new_book = Book(title, author)

        books.append(new_book)

        with open("books.txt", "a") as file:

            file.write(f"{title},{author},False\n")

        print("\n✅ Book added successfully!")

    
    elif choice == "2":

        if len(books) == 0:

            print("\nNo books available.")

        else:

            print("\n" + "=" * 60)
            print("                    BOOK LIST")
            print("=" * 60)

            for i, book in enumerate(books, start=1):

                status = "Issued" if book.issued else "Available"

                print(f"{i}. {book.title}")
                print(f"   Author : {book.author}")
                print(f"   Status : {status}")
                print("-" * 60)

    
    elif choice == "3":

        if len(books) == 0:

            print("\nNo books available.")

        else:

            for i, book in enumerate(books, start=1):

                status = "Issued" if book.issued else "Available"

                print(f"{i}. {book.title} ({status})")

            try:

                number = int(input("\nEnter book number to issue: "))

                if 1 <= number <= len(books):

                    if books[number - 1].issued:

                        print("\n❌ Book already issued.")

                    else:

                        books[number - 1].issued = True

                        print("\n✅ Book issued successfully!")

                else:

                    print("\nInvalid number.")

            except ValueError:

                print("\nEnter a valid number.")

    
    elif choice == "4":

        if len(books) == 0:

            print("\nNo books available.")

        else:

            for i, book in enumerate(books, start=1):

                status = "Issued" if book.issued else "Available"

                print(f"{i}. {book.title} ({status})")

            try:

                number = int(input("\nEnter book number to return: "))

                if 1 <= number <= len(books):

                    if books[number - 1].issued:

                        books[number - 1].issued = False

                        print("\n✅ Book returned successfully!")

                    else:

                        print("\nBook is already available.")

                else:

                    print("\nInvalid number.")

            except ValueError:

                print("\nEnter a valid number.")

    
    elif choice == "5":

        if len(books) == 0:

            print("\nNo books available.")

        else:

            for i, book in enumerate(books, start=1):

                print(f"{i}. {book.title}")

            try:

                number = int(input("\nEnter book number to delete: "))

                if 1 <= number <= len(books):

                    removed = books.pop(number - 1)

                    print(f"\n✅ '{removed.title}' deleted successfully!")

                else:

                    print("\nInvalid number.")

            except ValueError:

                print("\nEnter a valid number.")

    
    elif choice == "6":

        with open("books.txt", "w") as file:

            for book in books:

                file.write(f"{book.title},{book.author},{book.issued}\n")

        print("\nLibrary data saved successfully.")
        print("Thank you for using Library Management System!")

        break

    else:

        print("\n❌ Invalid choice!")