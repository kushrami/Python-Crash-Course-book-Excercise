#Pizza toppings:

user_toppings = ""

while user_toppings != "quit":
    user_toppings = input("Please enter your topping or enter 'quit' :")
    if user_toppings == 'quit':
        print()
    else:
        print("i will add topping of",user_toppings)