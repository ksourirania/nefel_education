# players = [
#     {
#     	"name": "Kevin Durant", 
#     	"age":34, 
#     	"position": "small forward", 
#     	"team": "Brooklyn Nets"
#     },
#     {
#     	"name": "Jason Tatum", 
#     	"age":24, 
#     	"position": "small forward", 
#     	"team": "Boston Celtics"
#     },
#     {
#     	"name": "Kyrie Irving", 
#     	"age":32, "position": "Point Guard", 
#     	"team": "Brooklyn Nets"
#     },
#     {
#     	"name": "Damian Lillard", 
#     	"age":33, "position": "Point Guard", 
#     	"team": "Portland Trailblazers"
#     },
#     {
#     	"name": "Joel Embiid", 
#     	"age":32, "position": "Power Foward", 
#     	"team": "Philidelphia 76ers"
#     },
#     {
#     	"name": "", 
#     	"age":16, 
#     	"position": "P", 
#     	"team": "en"
#     }
# ]

# Challenge 1: Update the Constructor
# Update the constructor to accept a dictionary with a single player's information instead of individual arguments for the attributes.

class Player:
    def __init__(self, player_dict ):
        self.name = player_dict["name"] 
        self.age =player_dict ["age"] 
        self.position =  player_dict ["position"]
        self.team = player_dict ["team"]
    def __repr__(self):
        return "Player:{},{} year, position: {},team: {}".format(self.name, self.age, self.position, self.team)
# Challenge 2: Create instances using individual player dictionaries.
# Given these variables, create Player instances for each of the following dictionaries.
#  Be sure to instantiate these outside the class definition, in the outer scope.



Jason={
       	"name": "Jason Tatum", 
     	"age":24, 
   	    "position": "small forward", 
    	"team": "Boston Celtics"
     }
print(Jason["name"])
Kevin={
    	"name": "Kevin Durant", 
     	"age":34, 
     	"position": "small forward", 
     	"team": "Brooklyn Nets"
    }
Kyrie={
     	"name": "Kyrie Irving", 
     	"age":32, "position": "Point Guard", 
     	"team": "Brooklyn Nets"
     }
Damain={
     	"name": "Damian Lillard", 
     	"age":33, "position": "Point Guard", 
     	"team": "Portland Trailblazers"
     }
Joel={
     	"name": "Joel Embiid", 
     	"age":32, "position": "Power Foward", 
     	"team": "Philidelphia 76ers"
     }




Jason_player = Player(Jason)
print(Jason_player)
Kevin_player = Player(Kevin)
print(Kevin_player)
Kyrie_player = Player(Kyrie)
print(Kyrie_player)
Damain_player = Player(Damain)
print(Damain_player)
Joel_player = Player(Joel)
print(Joel_player)







# Challenge 3: Make a list of Player instances from a list of dictionaries
# Finally, given the example list of players at the top of this module (the one with many players)
# write a for loop that will populate an empty list with Player objects from the original list of dictionaries.

players = [
    {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32, "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33, "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32, "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
    {
    	"name": "", 
    	"age":16, 
    	"position": "P", 
    	"team": "en"
    }
]
new_team=[]
for player_dict in players:
   player =Player(player_dict)
   new_team.append(player)
print(new_team)

# NINJA BONUS: Add a get_team(cls, team_list) @class method
# Add an @class method called get_team(cls, team_list) that, given a list of dictionaries populates
# and returns a new list of Player objects. Be sure to test your method!