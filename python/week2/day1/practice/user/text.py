# Attributes:
# On instantiation of a user, the following attributes should be passed in as arguments:

# first_name
# last_name
# email
# age
# Also include default attributes:
#  is_rewards_member - default value of False
# gold_card_points = 0
# Methods:


# spend_points(self, amount) - have this method decrease the user's points by the amount specified.

class user:
    def __init__(self , first_name, last_name , email ,age):
        self.first_name = first_name
        self.last_name = last_name
        self.email =email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    

# merhods
# display_info(self) - Have this method print all of the users' details on separate lines.
# enroll(self) - Have this method change the user's member status to True and set their gold card points to 200.

    def display_info(self):
        print(______)
        print(f"first name : {self.first_name}")
        print(f"last name:{self.last_name}")
        print(f"email:{self.email}")
        print(f"age:{self.age}")
        print(f"member:{self.is_rewards_member}")
        print(f"current points:{self.gold_card_points}")
        print(_______)

    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
    
    def spend_points(self , amount):
        if self.gold_card_points >= amount:
           self.gold_card_points -=amount
        else:
            print("not enough points to spends")


# Ninja Bonuses:

# Add logic in the enroll method to check if they are a member already, and if they are, print "User already a member." and return False, otherwise return True.
# Add logic in the spend points method to be sure they have enough points to spend that amount and handle appropriately.