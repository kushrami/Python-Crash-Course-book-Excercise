#Privileges:

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
        
class Admin(User):
    """Inherited class of User"""

    def __init__(self,first_name, last_name, age, gender):

        super().__init__(first_name, last_name, age, gender)
        self.privileges1 = Privileges()

class Privileges():
    """Saparate class for Privileges"""

    def __init__(self):

        self.privileges = ["can add post" , "can delete post" , "can ban user"]

    def show_privileges(self):
        """specific method to show privileges"""
        print("You have following privileges:")
        for privileg in self.privileges:
            print(privileg)

admin1 = Admin('tony','stark',32,'mr.')
admin1.privileges1.show_privileges()