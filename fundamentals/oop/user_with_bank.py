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


class User:
    def __init__(self, name, int_rate, balance):
        self.name = name
        self.account = BankAccount(int_rate, balance)
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    def make_withdrawl(self, amount):
        self.account.withdraw(amount)
        return self
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account.balance}")
        return self
    def transfer_money(self, other_user, amount):
        self.account.balance -= amount
        other_user.account.balance += amount
        return self

donovan = User('Donovan', 0.05, 500)
matthew = User('Matthew', 0.01, 1000)

donovan.display_user_balance()
matthew.display_user_balance()