
from transaction import Transaction
import datetime



class Account:
    """Represents a single bank account (e.g., Checking)."""

    def __init__(self, account_name):
        # Your code here:
        self.account_name=account_name
        self.transaction_list=[]


    def add_transaction(self, transaction):
        # Your code here:
        self.transaction_list.append(transaction)


    def get_balance(self):
        """Calculates and returns the current balance."""
        # Your code here:
        total_balance=0.0
        for transaction in self.transaction_list:
            total_balance+=transaction.amount
        return total_balance


    def __repr__(self):
        return f"Account('{self.account_name}')"



# 1. Create some transactions
t1 = Transaction(-50.00, "Groceries", "Weekly shopping")
t2 = Transaction(1500.00, "Salary", "Paycheck")
t3 = Transaction(-24.99, "Subscriptions", "Streaming service")

# 2. Create an account
my_checking = Account("My Checking Account")

# 3. Add transactions to the account
my_checking.add_transaction(t1)
my_checking.add_transaction(t2)
my_checking.add_transaction(t3)

# 4. Test the balance
#    (Should be: -50.00 + 1500.00 - 24.99 = 1425.01)
balance = my_checking.get_balance()
print(f"--- Account Report for: {my_checking.account_name} ---")
print(f"Current Balance: ${balance:.2f}")

print("\n--- Transaction History ---")
for t in my_checking.transaction_list:
    print(t)