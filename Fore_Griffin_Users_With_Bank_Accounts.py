# How to have a default value
#class methods
#static methods

class BankAccount:
    def __init__(self, name, interest_rate, balance):
        self.name = name
        #how interest rate with a default value, no need to enter a value how
        if interest_rate == None:
            self.interest_rate = 0.05
        else:
            self.interest_rate = interest_rate
        #how to set a default value
        if balance == None:
            self.balance = 0
        else:
            self.balance = balance
    
    def deposit(self,amount):
        self.balance += amount
        print(f"Made a Deposit. Balance: {self.balance}")
        return self
    
    def withdraw(self,amount):
        if(self.balance >= amount):
            self.balance -= amount
            print(f"Made a withdrawal. Balance: {self.balance}")
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5.00
        return self
    
    def display_account_info(self):
        print(f"Name: {self.name}, Balance: {self.balance}")
        return self
    
    def yield_interest(self):
        self.balance *= self.interest_rate
        print(f"Interest rate: {self.interest_rate}")
        print(f"Balance: {self.balance}")
        return self
    
account_1 = BankAccount("George", 0.05, 500)
account_2 = BankAccount("Riley", 0.06, 2700)

# account_1.deposit(50).deposit(300).deposit(400).withdraw(1000).yield_interest().display_account_info()
# account_2.deposit(100).deposit(100).withdraw(400).withdraw(400).withdraw(400).withdraw(400).yield_interest().display_account_info()


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        #how to link class,
        #how to have no need to input values
        self.account = BankAccount(name,0.05,0)

    def make_deposit(self,amount):
        self.account.deposit(amount)
        print(self.account.balance)
        return self

    def make_withdrawal(self,amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        #how to link method
        self.account.display_account_info()
        return self
    
    # subtract value of self, add value to parameter user
    def transfer_money(self,amount,user_2):
        self.account.balance -= amount
        user_2.account.balance += amount

#how to have multiple bank accounts one user
#how to transfer money between users

player_1 = User("Regina","rgina@mail.com")
player_2 = User("George","gcostanza@hotmail.net")
player_1.make_deposit(500).make_withdrawal(600).display_user_balance().transfer_money(30,player_2)
player_2.display_user_balance()