#Restaurant:

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

restaurant = Restaurant('startbucks','coffee')
print(restaurant.cuisine_type,restaurant.restaurant_name)
restaurant.describe_restaurant()
restaurant.open_restaurant()
