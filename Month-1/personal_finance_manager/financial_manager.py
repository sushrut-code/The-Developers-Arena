
import datetime
import pickle  # <-- Import the pickle library
import os  # <-- Import os to check if the file exists
from transaction import Transaction
from user import User
from account import Account




class FinanceManager:
    """Handles user registration, login, and data persistence."""

    def __init__(self, data_file):
        # Your code here:
        self.data_file=data_file
        self.users={}


    def register(self, username, password):
        """Registers a new user."""
        # Your code here:
        if username in self.users:
            print("User name already exists.")
            return

        new_user=User(username,password)
        self.users[username]=new_user
        print(f"User '{username}' registered successfully.")


    def login(self, username, password):
        """Logs in a user."""
        # Your code here:
        user = self.users.get(username)
        if user and user.password == password:
            print(f"Login successful! Welcome, {username}.")
            return user
        print("Invalid username or password.")
        return None


    def save_data(self):
        """Saves the self.users dictionary to a file using pickle."""
        with open(self.data_file, 'wb') as f:
            pickle.dump(self.users, f)
        print("Data saved successfully.")


    def load_data(self):
        """Loads the self.users dictionary from a file."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'rb') as f:
                self.users = pickle.load(f)
            print("Data loaded successfully.")
        else:
            print("No data file found. Starting with an empty system.")




print("--- SESSION 1: Registration ---")
manager = FinanceManager("my_finance_data.pkl")

# Register users
manager.register("Alice", "pass123")
manager.register("Bob", "abc")

# Add some data for Alice
user_alice = manager.login("Alice", "pass123")
if user_alice:
    user_alice.add_account("Checking")
    acct = user_alice.find_account("Checking")
    acct.add_transaction(Transaction(1000, "Salary", "Paycheck"))
    print(f"Alice's balance: {acct.get_balance()}")

# Save all data
manager.save_data()

print("\n--- SESSION 2: Loading Data ---")
# Create a NEW manager to simulate closing and re-opening the app
manager2 = FinanceManager("my_finance_data.pkl")

# Load the data from the file
manager2.load_data()

# Test logging in as Bob (who was saved)
user_bob = manager2.login("Bob", "abc")
print(f"Logged in user: {user_bob}")

# Test logging in as Alice and check her balance (should be 1000)
user_alice_2 = manager2.login("Alice", "pass123")
if user_alice_2:
    acct = user_alice_2.find_account("Checking")
    print(f"Loaded Alice's balance: {acct.get_balance()}")

# Test a bad login
print("\n--- Testing bad login ---")
bad_user = manager2.login("Alice", "wrongpass")
print(f"Logged in user: {bad_user}")