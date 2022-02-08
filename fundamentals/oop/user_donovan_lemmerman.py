class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
        return self
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

donovan = User('Donovan')
romero = User('Romero')
matthew = User('Matthew')

donovan.make_deposit(100).make_deposit(150).make_deposit(475).make_withdrawl(75).display_user_balance()

romero.make_deposit(100).make_deposit(200).make_withdrawl(50).make_withdrawl(50).display_user_balance()

matthew.make_deposit(750).make_withdrawl(50).make_withdrawl(100).make_withdrawl(200).display_user_balance()

donovan.transfer_money(matthew, 100)
donovan.display_user_balance()
matthew.display_user_balance()
