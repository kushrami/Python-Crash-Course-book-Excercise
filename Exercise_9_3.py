#Users:

class User():
    """ Making a USER class."""

    def __init__(self, first_name, last_name, age, gender):
        
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.gender = gender.title()

    def describe_user(self):
        """ Method for describing user profile."""

        print("First name :",self.first_name)
        print("Last name :",self.last_name)
        print("User's age :",self.age)
        print("User's Gender :",self.gender)
        
    def greet_user(self):
        """ Method for greeting the user"""
        print("welcome! Its nice to have you",self.gender,self.first_name,self.last_name)

user1 = User('Tony','stark',32,'mr.')
user2 = User('thor','The son of odin',1234,'mr.')
user3 = User('nessa','osoi',18,'ms.')

user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()