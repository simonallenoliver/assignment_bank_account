class BankAccount:

    def __init__(self, int_rate = .01, balance = 0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        print(self.balance)
        return self
    def yield_interest(self):
        self.balance += (self.balance * self.int_rate)
        return self

account1 = BankAccount()
account2 = BankAccount()

account1.deposit(20).deposit(35).deposit(22).withdraw(75).yield_interest().display_account_info()
account2.deposit(3033).deposit(3409).withdraw(250).withdraw(600).withdraw(300).withdraw(200).yield_interest().display_account_info()
