# Create a User class with an __init__ method

# Add a make_deposit method to the User class that calls on its bank account's instance methods.

# Add a make_withdrawal method to the User class that calls on its bank account's instance methods.

# Add a display_user_balance method to the User class that displays user's account balance

# SENSEI BONUS: Allow a user to have multiple accounts; update methods so the user has to specify which account they are withdrawing or depositing to

# SENPAI BONUS: Add a transfer_money(self, amount, other_user) method to the user class that takes an amount and a different User instance, and transfers money from the user's account into another user's account.

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    # other methods
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    	# your code here
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    
    def display_user_balance(self):
        print(self.name)
        self.account.display_account_info()
        return self




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
            self.balance-= 5
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
    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()
    
    # user
user1 = User ("mira" , "mm@.com")
user1.make_deposit(200).make_deposit(150)
print(user1.account.balance)
user2 = User ("lili" , "ll@.com")
user2.make_deposit(2400).make_deposit(50)
print(user2.account.balance)



    
    

