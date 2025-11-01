class Account:
    def __init__(self,owner,account_number,initial_deposit=0):
        self.owner_name=owner
        self.account_number=account_number
        self.balance=initial_deposit
        print(f"Account for {self.owner_name} (ID: {self.account_number}) created with ${self.balance}.")

    def deposit(self,amount):
        self.balance+=amount
        print(f"Deposited ${amount}. New balance: ${self.balance}.")

    def withdraw(self,amount):
        if amount>self.balance:
            print("Error: Insufficient balance.")
        else:
            self.balance-=amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}.")

    def get_balance(self):
        print(f"Current balance for {self.account_number}: ${self.balance}.")
        return self.balance