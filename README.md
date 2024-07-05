# Bank Account Management System

A simple bank account management system written in Python.

## Features

- Create new bank accounts with unique account numbers and initial balances.
- Deposit funds into existing accounts.
- Withdraw funds from existing accounts, ensuring sufficient balance.
- Display account information, including account number, account holder, and current balance.
- Remove existing accounts.

## Usage

1. Run the program using Python.
2. Follow the on-screen prompts to interact with the bank account management system.
3. Choose the desired option from the menu:
   - 1: Create a new account
   - 2: Deposit funds into an existing account
   - 3: Withdraw funds from an existing account
   - 4: Display account information
   - 5: Remove an existing account
   - 6: Exit the program

## Example

```
Welcome to the Bank Account Management System!

Choose an option:
1. Create Account
2. Deposit
3. Withdraw
4. Display Account Info
5. Remove Account
6. Exit

Enter your choice: 1
Enter account number: 12345
Enter account holder: John Doe
Enter initial balance: 1000.00
Account created successfully!

Choose an option:
1. Create Account
2. Deposit
3. Withdraw
4. Display Account Info
5. Remove Account
6. Exit

Enter your choice: 4
Enter account number: 12345
Account Number: 12345
Account Holder: John Doe
Current Balance: $1000.00

Choose an option:
1. Create Account
2. Deposit
3. Withdraw
4. Display Account Info
5. Remove Account
6. Exit

Enter your choice: 6
Thank you for using the Bank Account Management System!
```

## Note

This program does not persist data between runs. If you want to save account information, you can modify the program to use a database or a file to store the account data.