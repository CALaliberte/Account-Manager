# Account-Manager

A simple bank account manager written in Python.

## Features

- Create new bank accounts with unique account numbers and initial balances.
- Deposit funds into existing accounts.
- Withdraw funds from existing accounts, ensuring sufficient balance.
- Display account information, including account number, account holder, and current balance.

## Usage

1. Run the program using Python.
2. Follow the on-screen prompts to interact with the bank account manager.
3. Choose the desired option from the menu:
   - 1: Create a new account
   - 2: Deposit funds into an existing account
   - 3: Withdraw funds from an existing account
   - 4: Display account information
   - 5: Exit the program

## Example

```
1. Create Account
Enter account number: 12345
Enter account holder: John Doe
Enter initial balance: 1000.00
Account created successfully!

1. Create Account
Enter account number: 67890
Enter account holder: Jane Smith
Enter initial balance: 500.00
Account created successfully!

2. Deposit
Enter account number: 12345
Enter deposit amount: 500.00
Deposit successful!

3. Withdraw
Enter account number: 67890
Enter withdrawal amount: 200.00
Withdrawal successful!

4. Display Account Info
Enter account number: 12345
Account Number: 12345
Account Holder: John Doe
Current Balance: $1500.00

5. Exit
```

## Note

This program does not persist data between runs. If you want to save account information, you can modify the program to use a database or a file to store the account data.