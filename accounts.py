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
    accounts = []

    while True:
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Display Account Info")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            account_number = input("Enter account number: ")
            account_holder = input("Enter account holder: ")
            initial_balance = float(input("Enter initial balance: "))
            account = BankAccount(account_number, account_holder, initial_balance)
            accounts.append(account)
            print("Account created successfully!")
        elif choice == 2:
            account_number = input("Enter account number: ")
            for account in accounts:
                if account.getAccountNumber() == account_number:
                    amount = float(input("Enter deposit amount: "))
                    if amount > 0:
                        account.deposit(amount)
                        print("Deposit successful!")
                    else:
                        print("Error: Deposit amount must be a positive number.")
                    break
            else:
                print("Account not found.")
        elif choice == 3:
            account_number = input("Enter account number: ")
            for account in accounts:
                if account.getAccountNumber() == account_number:
                    amount = float(input("Enter withdrawal amount: "))
                    if amount > 0:
                        if amount <= account.getBalance():
                            account.withdraw(amount)
                            print("Withdrawal successful!")
                        else:
                            print("Error: Insufficient balance.")
                    else:
                        print("Error: Withdrawal amount must be a positive number.")
                    break
            else:
                print("Account not found.")
        elif choice == 4:
            account_number = input("Enter account number: ")
            for account in accounts:
                if account.getAccountNumber() == account_number:
                    print(account.displayAccountInfo())
                    break
            else:
                print("Account not found.")
        elif choice == 5:
            break
        else:
            print("Error: Invalid choice.")

if __name__ == "__main__":
    main()