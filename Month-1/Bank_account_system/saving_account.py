from account import Account


class SavingsAccount(Account):

    def __init__(self, owner_name, account_number, interest_rate, initial_deposit=0):

        super().__init__(owner_name,account_number,initial_deposit=0)
        self.interest_rate=interest_rate

    def apply_interest(self):
        # Your code here:
        interest=self.balance*self.interest_rate
        self.balance+=interest
        print(f"Interest of ${interest} applied. New balance: ${self.balance}.")



print("\n--- Creating Savings Account ---")
s_acct = SavingsAccount("Alice", "S123", 0.05, 1000)  # 5% interest rate, $1000 deposit


print("\n--- Testing Inherited Methods ---")
s_acct.get_balance()
s_acct.deposit(200)
s_acct.withdraw(50)


print("\n--- Testing New Method ---")
# Current balance should be 1000 + 200 - 50 = 1150
# Interest should be 1150 * 0.05 = 57.5
# New balance should be 1150 + 57.5 = 1207.5
s_acct.apply_interest()
s_acct.get_balance()


