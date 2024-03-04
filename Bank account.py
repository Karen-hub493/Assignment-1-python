#Program to calculate bank account
import datetime

class BankAccount:
    def __init__(self, account_number, balance, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.customer_name = customer_name

    def deposit(self, amount):
        self.balance += amount
        return amount

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return amount

    def check_balance(self):
        print("Current balance:", self.balance)

    def customer_details(self):
        print("Customer Name:", self.customer_name)
        print("Account Number:", self.account_number)
        print("Date of Account Opening:", self.date_of_opening)
        print("Current Balance:", self.balance)

# Create an instance of BankAccount class
bank_acc = BankAccount(account_number="123456789", balance=1000, customer_name="John Doe")

# Perform operations
print("Deposited amount:", bank_acc.deposit(500))
print("Withdrawn amount:", bank_acc.withdraw(300))
bank_acc.check_balance()
bank_acc.customer_details()
