class BankAccount:
    accounts = []
    def __init__(self,int_rate,account):
        self.int_rate = int_rate
        self.account = account
        BankAccount.accounts.append(self)

    def deposit(self,amount):
        self.account += amount
        return self

    def withdraw(self,amount):
        if(self.account - amount) >= 0:
            self.account -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.account -= 5
        return self

    def display_account_info(self):
        print(f'Balance: {self.account}')
        return self

@classmethod
def print_all_accounts(cls):
        for accounts in cls.accounts:
            accounts.display_account_info()

savings = BankAccount(0.05,1200)
checking = BankAccount(0.03,800)

savings.deposit(200).deposit(100).deposit(300).withdraw(500).yield_interest().display_account_info()
checking.deposit(60).deposit(30).withdraw(80).withdraw(240).withdraw(160).withdraw(40).yield_interest().display_account_info()

BankAccount.print_all_accounts()

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = 0

    def make_deposit(self, amount):
        self.account += amount
        return self
    
    def make_withdrawal(self, amount):
        self.account -= amount
        return self

    def display_user_balance(self):
        print(f'User: {self.name} Balance: ${self.account}')
        return self

    def transfer_money(self, amount, other):
        self.account_balance -= amount
        other.account_balance += amount
        self.display_user_balance()
        other.display_user_balance()
        return self

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
ichigo = User("Kurosaki Ichigo", "ichigo@bleach.com")