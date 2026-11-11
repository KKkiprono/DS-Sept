# Mini banking system

balance = 5000
user_pin = "1234@k"
attempts = 0 

def check_balance(): 
    print(f"Your current balance is Kshs. {balance}")
def deposit():
    global balance
    amount = float(input("Enter the amount to deposit: "))
    if amount > 0:
        balance = balance + amount
        print(f"Kshs. {amount} deposited successfully.")
        print(f"Balance: {balance}")
    else: 
        print("Invalid amount. Enter an amount greater than zero")
def withdraw():
    global balance
    amount = float(input("Enter the amount to withdraw: "))
    if amount < 0:
        print("Invalid amount.")
    elif amount > balance:
        print("Insufficient balance. ")
    else:
        balance = balance - amount
        print(f"Kshs. {amount} withdrawn successfully.")
        print(f"Balance:{balance}")
def menu():
    while True: 
        print()
        print("Welcome to the Main Menu")
        print("1. Check balance")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            print("Thank you for using the mini bank")
            break
        else:
            print("Invalid option. Pick option (1-4)")

while attempts < 5:
    pin = input("Enter your user pin: ")
    if pin == user_pin: 
        print("Login successful")
        menu()
        break
    else: 
        print("Incorrect pin")
        attempts = attempts + 1
        remaining = 5 - attempts
        print(f"Attempts remaining: {remaining}")
        
    