from account import Account
from saving_account import SavingsAccount


class CheckingAccount(Account):

    def __init__(self, owner_name, account_number, overdraft_limit, initial_deposit=0):
        super().__init__(owner_name,account_number,initial_deposit=0)
        self.overdraft_limits=overdraft_limit



    def withdraw(self, amount):
        # Your code here:
        # 1. Check if the amount is positive. If not, print an error.
        if amount<=0:
            print("Error: Enter positive amount.")
            return
        if amount<=(self.balance + self.overdraft_limits):
            self.balance -= amount
            print(f"withdrew ${amount}. New balance: ${self.balance}")

        else:
            print("Error: Insufficient balance.")
            return







print("\n--- Creating Checking Account ---")
c_acct = CheckingAccount("Bob", "C456", 500, 1000)  # $500 overdraft, $1000 deposit


print("\n--- Testing Inherited Methods ---")
c_acct.get_balance()
c_acct.deposit(300)


print("\n--- Testing Overridden Method ---")
# Current balance is 1000 + 300 = 1300. Overdraft limit is 500.
# Max withdrawal should be 1300 + 500 = 1800.

print("\nAttempting to withdraw $1500 (should succeed)...")
c_acct.withdraw(1500)
# New balance should be 1300 - 1500 = -200
c_acct.get_balance()

print("\nAttempting to withdraw $400 (should fail)...")
# Current balance is -200. Overdraft limit is 500.
# Max withdrawal is -200 + 500 = 300.
# 400 is > 300, so it should fail.
c_acct.withdraw(400)
c_acct.get_balance()

print("\nAttempting to withdraw $250 (should succeed)...")
c_acct.withdraw(250)
# New balance should be -200 - 250 = -450
c_acct.get_balance()