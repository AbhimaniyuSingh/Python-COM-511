''' 1. Write a Python program that allows a librarian to add several books to a library. For each book, ask the user to enter its title and the number of copies. Store each book and its available copy count in a dictionary.

After the books have been added, display a menu that lets the user issue a book, return a book, display all books, or exit the program.
Apply these conditions:

* Book titles should be compared without distinguishing uppercase and lowercase letters.
* A book can be issued only if it exists in the library and at least one copy is available.
* Issuing a book decreases its available copy count by one.
* A book can be returned only if it exists in the library and at least one copy has already been issued.
* Returning a book increases its available copy count by one.
* Display an appropriate message for an unavailable book, an invalid choice, or an invalid number of copies.'''


class Library:
    def __init__(self):
        self.books = {}
        self.issued = {}

    def addbooks(self):
        n = int(input("Enter the no of books: "))
        for i in range(n):
            title = input("Enter book title: ").lower()
            copies = int(input("Enter no of copies: "))

            if copies <= 0:
                print("Invalid number of copies")
            else:
                self.books[title] = self.books.get(title, 0) + copies

    def issue_book(self):
        title = input("Enter book to issue: ").lower()
        if title not in self.books:
            print("Book not found!")
        elif self.books[title] > 0:
            self.books[title] -= 1
            self.issued[title] = self.issued.get(title, 0) + 1
            print("Book issued successfully!")
        else:
            print("No copies available!")

    def returnbooks(self):
        title = input("Enter book to return: ").lower()
        if title not in self.books:
            print("Book not found!")
        elif self.issued.get(title, 0) > 0:
            self.books[title] += 1
            self.issued[title] -= 1
            print("Book returned successfully!")
        else:
            print("No copies have been issued!")

    def display(self):
        if not self.books:
            print("No books in library!")
        else:
            for title, copies in self.books.items():
                print(title, ":", copies, "copies")

library = Library()
library.addbooks()

while True:
    print("\n1. Issue Book\n2. Return Book\n3. Display Books\n4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        library.issue_book()
    elif choice == '2':
        library.returnbooks()
    elif choice == '3':
        library.display()
    elif choice == '4':
        break
    else:
        print("Invalid choice!")
