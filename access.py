def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == "admin" and password == "1234":
        print("Login successful")
    else:
        print("Invalid credentials")

login()

def welcome():
    print("Welcome to our Login System!")

welcome()