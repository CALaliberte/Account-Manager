class BankAccount:
    def __init__(self, accountNumber, accountHolder, initialBalance):
        self.__accountNumber = accountNumber
        self._accountHolder = accountHolder
        self.__balance = initialBalance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Error: Deposit amount must be a positive number.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
            else:
                print("Error: Insufficient balance.")
        else:
            print("Error: Withdrawal amount must be a positive number.")

    def getBalance(self):
        return self.__balance

    def getAccountNumber(self):
        return self.__accountNumber

    def displayAccountInfo(self):
        return f"Account Number: {self.__accountNumber}\nAccount Holder: {self._accountHolder}\nCurrent Balance: ${self.__balance:.2f}"


def main():
    accounts = {}

    print("Welcome to the Bank Account Management System!")

    while True:
        print("\nChoose an option:")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Display Account Info")
        print("5. Remove Account")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")
            continue

        if choice == 1:
            while True:
                try:
                    account_number = int(input("Enter account number: "))
                    break
                except ValueError:
                    print("Error: Account number must be an integer.")

            while True:
                try:
                    account_holder = input("Enter account holder: ")
                    if account_holder.replace(" ", "").replace("'", "").isalpha():
                        break
                    else:
                        raise ValueError                        
                except ValueError:
                    print("Error: Invalid input. Please enter a valid name (only letters).")
            
            while True:
                try:
                    initial_balance = float(input("Enter initial balance: "))
                    break
                except ValueError:
                    print("Error: Invalid input. Please enter a valid number.")

            if account_number in accounts:
                print("Error: Account already exists.")
            else:
                account = BankAccount(account_number, account_holder, initial_balance)
                accounts[account_number] = account
                print("Account created successfully!")
                
        elif choice == 2:
            account_number = int(input("Enter account number: "))
            if account_number in accounts:
                while True:
                    try:
                        amount = float(input("Enter deposit amount: "))
                        break
                    except ValueError:
                        print("Error: Invalid input. Please enter a valid number.")

                if amount > 0:
                    accounts[account_number].deposit(amount)
                    print("Deposit successful!")
                else:
                    print("Error: Deposit amount must be a positive number.")
            else:
                print("Account not found.")
        
        elif choice == 3:
            account_number = int(input("Enter account number: "))
            if account_number in accounts:
                while True:
                    try:
                        amount = float(input("Enter withdrawal amount: "))
                        break
                    except ValueError:
                        print("Error: Invalid input. Please enter a valid number.")

                if amount > 0:
                    if amount <= accounts[account_number].getBalance():
                        accounts[account_number].withdraw(amount)
                        print("Withdrawal successful!")
                    else:
                        print("Error: Insufficient balance.")
                else:
                    print("Error: Withdrawal amount must be a positive number.")
            else:
                print("Account not found.")
        
        elif choice == 4:
            account_number = int(input("Enter account number: "))
            if account_number in accounts:
                print(accounts[account_number].displayAccountInfo())
            else:
                print("Account not found.")
        
        elif choice == 5:
            account_number = int(input("Enter account number: "))
            if account_number in accounts:
                del accounts[account_number]
                print("Account removed successfully!")
            else:
                print("Account not found.")
        
        elif choice == 6:
            print("Thank you for using the Bank Account Management System!")
            break
        else:
            print("Error: Invalid choice.")

if __name__ == "__main__":
    main()