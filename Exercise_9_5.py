#login attempts:

class User():
    """ Making a USER class."""

    def __init__(self, first_name, last_name, age, gender):
        
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.gender = gender.title()
        self.login_attempts = 0

    def describe_user(self):
        """ Method for describing user profile."""

        print("First name :",self.first_name)
        print("Last name :",self.last_name)
        print("User's age :",self.age)
        print("User's Gender :",self.gender)
        
    def greet_user(self):
        """ Method for greeting the user"""
        print("welcome! Its nice to have you",self.gender,self.first_name,self.last_name)

    def increment_login_attempts(self):
        """Method to increment login attempt"""
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """Method to reset login attempt"""
        self.login_attempts = 0
        
user1 = User('Tony','stark',32,'mr.')

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(str(user1.login_attempts)+" times you have logged in.")
user1.reset_login_attempts()
print(str(user1.login_attempts)+" times you have logged in.")