
import datetime
import pickle
import os
from transaction import Transaction
from user import User
from account import Account
from financial_manager import FinanceManager


def main():
    """The main function to run the Personal Finance Manager CLI."""

    DATA_FILE = "finance_manager_data.pkl"
    manager = FinanceManager(DATA_FILE)
    manager.load_data()

    current_user = None

    # --- MAIN APPLICATION LOOP (Outer loop) ---
    while True:
        if current_user is None:
            # --- LOGIN/REGISTER MENU ---
            print("\n--- Personal Finance Manager ---")
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                # --- Register ---
                username = input("Enter new username: ")
                password = input("Enter new password: ")
                manager.register(username, password)
                manager.save_data()  # Save after registering

            elif choice == '2':
                # --- Login ---
                username = input("Enter username: ")
                password = input("Enter password: ")
                current_user = manager.login(username, password)

            elif choice == '3':
                # --- Exit ---
                print("Goodbye!")
                break

            else:
                print("Invalid choice.")

        else:
            # --- LOGGED-IN MENU (Inner loop) ---
            print(f"\n--- Welcome, {current_user.username}! ---")
            print("1. Add a new Account")
            print("2. Add a Transaction")
            print("3. View Account Balance")
            print("4. View Transaction History")
            print("5. Logout")
            choice = input("Enter your choice: ")

            if choice == '1':
                # --- Add Account ---
                account_name = input("Enter new account name (e.g., Checking, Savings): ")
                current_user.add_account(account_name)
                manager.save_data()

            elif choice == '2':
                # --- Add Transaction ---
                account_name = input("Enter account to add transaction to: ")
                acct = current_user.find_account(account_name)

                if acct is None:
                    print("Error: Account not found.")
                    continue

                try:
                    amount = float(input("Enter amount (use '-' for expenses, e.g., -50.25): "))
                except ValueError:
                    print("Error: Invalid amount.")
                    continue

                category = input("Enter category (e.g., Groceries, Salary): ")
                description = input("Enter description: ")

                t = Transaction(amount, category, description)
                acct.add_transaction(t)
                print("Transaction added.")
                manager.save_data()

            elif choice == '3':
                # --- View Balance ---
                account_name = input("Enter account name to view balance: ")
                acct = current_user.find_account(account_name)

                if acct:
                    print(f"Balance for {acct.account_name}: ${acct.get_balance():.2f}")
                else:
                    print("Error: Account not found.")

            elif choice == '4':
                # --- View History (Reporting) ---
                account_name = input("Enter account name to view history: ")
                acct = current_user.find_account(account_name)

                if acct:
                    print(f"\n--- Transaction History for {acct.account_name} ---")
                    if not acct.transaction_list:
                        print("No transactions found.")
                    else:
                        for t in acct.transaction_list:
                            print(t)
                    # Print a summary balance
                    print(f"--- Current Balance: ${acct.get_balance():.2f} ---")
                else:
                    print("Error: Account not found.")

            elif choice == '5':
                # --- Logout ---
                print(f"Logging out {current_user.username}...")
                current_user = None  # This sends the loop back to the login menu

            else:
                print("Invalid choice.")


# --- This runs the main function when you run the script ---
if __name__ == "__main__":
    main()