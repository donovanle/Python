class BankAccount:
    accounts = []
    def __init__(self, int_rate, balance): 
        self.interest = int_rate
        self.balance = balance
        if balance is None:
            self.balance = 0
        BankAccount.accounts.append(self)
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            print("Insufficeint funds: Charging a $5 fee")
            self.balance -= 5
        return self
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.interest
        else:
            print("Account below $0's")
        return self
    @classmethod
    def print_account(cls):
        for i in cls.accounts:
            print(f"Balance : {i.balance}")
            print(f"Intrest : {i.interest}")




donovan = BankAccount(0.05, 500)
matthew = BankAccount(0.1, 1000)
donovan.deposit(300).deposit(100).deposit(50).yield_interest().display_account_info()
matthew.deposit(500).deposit(1300).withdraw(40).withdraw(68).withdraw(145).withdraw(358).yield_interest().display_account_info()
BankAccount.print_account()