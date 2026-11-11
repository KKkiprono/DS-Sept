books = {
    "maths": "available",
    "kiswahili": "available",
    "science": "available",
    "statistics": "available"
}
borrowed = {}

librarian_password = "lib123"
is_librarian = False
total_borrowed = 0


def display_books():
    print("books in the library:")
    for title in books:
        print(f"- {title}: {books[title]}")


def borrow_book():
    global total_borrowed
    student = input("enter your name: ")
    if student not in borrowed:
        borrowed[student] = []

    if len(borrowed[student]) >= 2:
        print("you can only borrow 2 books at a time")
        return

    title = input("enter book title to borrow: ")
    if title not in books:
        print("book not found")
    elif books[title] == "borrowed":
        print("sorry, that book is not available")
    else:
        books[title] = "borrowed"
        borrowed[student].append(title)
        total_borrowed = total_borrowed + 1
        print(f"{student} borrowed {title}")


def return_book():
    global total_borrowed
    student = input("enter your name: ")
    title = input("enter book title to return: ")
    if student in borrowed and title in borrowed[student]:
        borrowed[student].remove(title)
        books[title] = "Available"
        total_borrowed = total_borrowed - 1
        print(f"{title} returned successfully")
    else:
        print("you did not borrow that book")


def librarian_login():
    global is_librarian
    for i in range(3):
        if input("enter librarian password: ") == librarian_password:
            is_librarian = True
            print("librarian access granted")
            return
        print("wrong password")
    print("too many wrong attempts")


def librarian_menu():

    if not is_librarian:
        print("librarian access only. Please log in first")
        return
    print("1. view who borrowed what")
    print("2. add a new book")
    choice = input("Choose: ")
    if choice == "1":
        print(f"total books borrowed: {total_borrowed}")
        for student in borrowed:
            print(f"{student}: {borrowed[student]}")
    elif choice == "2":
        title = input("enter new book title: ")
        books[title] = "available"
        print(f"{title} added")
    else:
        print("invalid choice")


while True:
    print("library Management System")
    print("1. display books")
    print("2. borrow a book")
    print("3. return a book")
    print("4. librarian login")
    print("5. librarian menu")
    print("6. exit")
    option = input("choose: ")

    if option == "1":
        display_books()
    elif option == "2":
        borrow_book()
    elif option == "3":
        return_book()
    elif option == "4":
        librarian_login()
    elif option == "5":
        librarian_menu()
    elif option == "6":
        print("Goodbye")
        break
    else:
        print("Invalid choice")
