class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited:", amount)
            print("Current Balance:", self.balance)
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
            print("Current Balance:", self.balance)
        else:
            print("Invalid withdrawal or insufficient balance")

    def display_balance(self):
        print("Account Number:", self.account_number)
        print("Account Holder:", self.account_holder)
        print("Balance:", self.balance)

account = BankAccount("123456", "Alice", 1000)

account.display_balance()
account.deposit(500)
account.withdraw(300)
account.display_balance()
