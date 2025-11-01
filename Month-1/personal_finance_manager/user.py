
import datetime
from transaction import Transaction
from account import Account



class User:
    """Manages all accounts and data for a single user."""

    def __init__(self, username, password):
        # Your code here:
        self.username=username
        self.password=password
        self.accounts={}


    def add_account(self, account_name):
        """Creates a new Account object and adds it to the user."""
        # Your code here:
        if account_name in self.accounts:
            print("Error: account already added..")
            return
        new_acct=Account(account_name)
        self.accounts[account_name]=new_acct
        print("Account successfully added!!")




    def find_account(self, account_name):
        """Finds and returns an account object by its name."""
        # Your code here:
        return self.accounts.get(account_name)


    def __repr__(self):
        return f"User('{self.username}', {len(self.accounts)} accounts)"



# 1. Create a user
user1 = User("Alice", "password123")
print(user1)

# 2. Add accounts
print("\nAdding accounts...")
user1.add_account("Checking")
user1.add_account("Savings")
user1.add_account("Credit Card")

# 3. Try to add a duplicate (should fail)
print("\nAdding duplicate...")
user1.add_account("Checking")

# 4. Find an account
print("\nFinding account...")
checking_acct = user1.find_account("Checking")
if checking_acct:
    print(f"Found account: {checking_acct.account_name}")
else:
    print("Account not found.")

# 5. Add a transaction to the found account
if checking_acct:
    t1 = Transaction(-75.00, "Gas", "Filled up car")
    checking_acct.add_transaction(t1)
    print(f"Balance for 'Checking': ${checking_acct.get_balance():.2f}")

# 6. Check balance of another account
savings_acct = user1.find_account("Savings")
if savings_acct:
    print(f"Balance for 'Savings': ${savings_acct.get_balance():.2f}")