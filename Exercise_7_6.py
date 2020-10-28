#three exits:
# will take excercise 7-4

#Pizza toppings:

user_toppings = ""
Flag = True
while Flag:
    user_toppings = input("Please enter your topping or enter 'quit' :")
    if user_toppings == 'quit':
        Flag = False
        break
    else:
        print("i will add topping of",user_toppings)