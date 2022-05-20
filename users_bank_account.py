class BankAccount:
    accounts = []
    def __init__(self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self,amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        return f"{self.balance}"

    def yeild_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

class User:
    def __init__(self, name):
        self.name = name
        self.account = {
            "savings" : BankAccount(0.05,1200),
            "checking" : BankAccount(0.03,800)}

    def display_user_balance(self):
        print(f"User: {self.name}, Savings Balance: {self.account['savings'].display_account_info()}")
        print(f"User: {self.name}, Checking Balance: {self.account['checking'].display_account_info()}")
        return self

    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()
        return self

ichigo = User("Ichigo")

ichigo.account['checking'].deposit(200)
ichigo.display_user_balance()        