#Icecream stand

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

class IceCreamStand(Restaurant):
    """Inherited class of restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = ['banana','coco','kiwi']

    def display_flavours(self):
        print("Available Flavours:\n",self.flavours)

myicecream = IceCreamStand('mucine','icecream')
myicecream.display_flavours()