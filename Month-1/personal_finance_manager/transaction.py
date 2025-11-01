import datetime


class Transaction:
    """Represents a single transaction (income or expense)."""

    def __init__(self, amount, category, description, date=None):
        # Your code here:
        self.amount=amount
        self.category=category
        self.description=description
        if date is None:
            self.date=datetime.date.today()
        else:
            self.date=date


    def __repr__(self):
        """A 'representation' to make printing easy."""
        # This shows a '+' for income, and nothing for expenses
        sign = '+' if self.amount > 0 else ''
        # .2f formats the float to 2 decimal places (like $1500.00)
        return f"[{self.date}] {self.category}: {sign}${self.amount:.2f} ({self.description})"



t1 = Transaction(-50.00, "Groceries", "Weekly shopping")
t2 = Transaction(1500.00, "Salary", "Paycheck")
t3 = Transaction(-24.99, "Subscriptions", "Streaming service")

print("--- Your Transactions ---")
print(t1)
print(t2)
print(t3)