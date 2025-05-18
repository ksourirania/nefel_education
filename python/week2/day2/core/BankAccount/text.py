class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.it_rate= int_rate
        self.balance=balance
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
        return self
        # your code here
    def withdraw(self, amount):
        if(self.balance- amount)>=0:
            self.balance-= amount
        else:
            print(f"Insufficient funds: Charging a $5 fee")
            self.balance-= amount
        return self
            
        # your code here
    def display_account_info(self):
        print(f"balance:{self.balance}")
        return self
        # your code here
    def yield_interest(self):
        if self.balance>0:
            self.balance+=(self.balance*self.it_rate)
            return self
savingAccount= BankAccount(1,1200)
chakingAccount=BankAccount(2 ,3000)
savingAccount.deposit(20).deposit(60).deposit(50).withdraw(600).yield_interest().display_account_info()
chakingAccount.deposit(10).deposit(40).deposit(20).withdraw(100).yield_interest().display_account_info()
        # your code here
