#Three Restaurant:

class Restaurant():
    """A simple attempt to make class restaurant. """

    def __init__(self, restaurant_name, cuisine_type):
        """ This is to initialize name and type of restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """ This method describes the Restaurant"""
        print("Restaurant name :",self.restaurant_name.title())
        print("Its Cuisine Type:",self.cuisine_type.title())

    def open_restaurant(self):
        print("The restaurant is open.")

restaurant1 = Restaurant('startbucks','coffee')
restaurant2 = Restaurant('macdonalds','burger')
restaurant3 = Restaurant('meghana','biryani')

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()