from account import Account
from saving_account import SavingsAccount
from checking_account import CheckingAccount


def main():
    """Main function to run the bank CLI."""
    accounts = {}
    print("Welcome to the Bank!")

    while True:
        print("\n--- Bank Menu ---")
        print("1. Create a new Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Apply Interest (Savings Accounts only)")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            # --- Create Account ---
            print("\n--- Create New Account ---")
            owner_name = input("Enter owner's name: ")
            account_number = input("Enter new account number: ")

            if account_number in accounts:
                print("Error: This account number already exists.")
                continue

            try:
                initial_deposit = float(input("Enter initial deposit (0 or more): "))
                if initial_deposit < 0:
                    print("Error: Initial deposit cannot be negative.")
                    continue
            except ValueError:
                print("Error: Invalid deposit amount. Must be a number.")
                continue

            acct_type = input("Account type (checking/savings): ").lower()

            if acct_type == 'savings':
                try:
                    interest_rate = float(input("Enter interest rate (e.g., 0.05 for 5%): "))
                    if interest_rate < 0:
                        print("Error: Interest rate cannot be negative.")
                        continue
                except ValueError:
                    print("Error: Invalid interest rate.")
                    continue

                # Create and store the new SavingsAccount
                new_account = SavingsAccount(owner_name, account_number, interest_rate, initial_deposit)
                accounts[account_number] = new_account
                print(f"Savings account '{account_number}' created.")

            elif acct_type == 'checking':
                try:
                    overdraft_limit = float(input("Enter overdraft limit (e.g., 500): "))
                    if overdraft_limit < 0:
                        print("Error: Overdraft limit cannot be negative.")
                        continue
                except ValueError:
                    print("Error: Invalid overdraft limit.")
                    continue

                # Create and store the new CheckingAccount
                new_account = CheckingAccount(owner_name, account_number, overdraft_limit, initial_deposit)
                accounts[account_number] = new_account
                print(f"Checking account '{account_number}' created.")

            else:
                print("Error: Invalid account type. Please choose 'checking' or 'savings'.")

        elif choice == '2':
            # --- Deposit ---
            print("\n--- Deposit ---")
            account_number = input("Enter account number: ")
            account = accounts.get(account_number)

            if account:
                try:
                    amount = float(input("Enter amount to deposit: "))
                    account.deposit(amount)
                except ValueError:
                    print("Error: Invalid amount. Please enter a number.")
            else:
                print("Error: Account not found.")

        elif choice == '3':
            # --- Withdraw ---
            print("\n--- Withdraw ---")
            account_number = input("Enter account number: ")
            account = accounts.get(account_number)

            if account:
                try:
                    amount = float(input("Enter amount to withdraw: "))
                    account.withdraw(amount)
                except ValueError:
                    print("Error: Invalid amount. Please enter a number.")
            else:
                print("Error: Account not found.")

        elif choice == '4':
            # --- Check Balance ---
            print("\n--- Check Balance ---")
            account_number = input("Enter account number: ")
            account = accounts.get(account_number)

            if account:
                account.get_balance()  # Just call the method
            else:
                print("Error: Account not found.")

        elif choice == '5':
            # --- Apply Interest ---
            print("\n--- Apply Interest ---")
            account_number = input("Enter SAVINGS account number: ")
            account = accounts.get(account_number)

            if account:
                if isinstance(account, SavingsAccount):
                    account.apply_interest()
                else:
                    print("Error: Interest can only be applied to savings accounts.")
            else:
                print("Error: Account not found.")

        elif choice == '6':
            # --- Exit ---
            print("Thank you for banking with us. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")



main()
