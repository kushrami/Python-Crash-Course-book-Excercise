#Number served:
#Restaurant:

class Restaurant():
    """A simple attempt to make class restaurant. """

    def __init__(self, restaurant_name, cuisine_type):
        """ This is to initialize name and type of restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """ This method describes the Restaurant"""
        print("Restaurant name :",self.restaurant_name.title())
        print("Its Cuisine Type:",self.cuisine_type.title())
        
    def open_restaurant(self):
        print("The restaurant is open.")

    def set_number_served(self,number_of_customers):
        """method to set number of customers served"""
        self.number_served = number_of_customers
    
    def increment_number_served(self,number_of_customers):
        """method to increment number of customers served"""
        self.number_served += number_of_customers


restaurant = Restaurant('startbucks','coffee')
print("They have served around "+str(restaurant.number_served)+" people.")
restaurant.number_served = 1000
print("They have served around "+str(restaurant.number_served)+" people.")

restaurant.set_number_served(2121)
print("They have served around "+str(restaurant.number_served)+" people.")

restaurant.increment_number_served(100)
print("They have served around "+str(restaurant.number_served)+" people till day.")
