#movie tickets:

age = 0

while True:
    age = int(input("Please enter your age:"))
    if age < 3:
        print("You have to pay nothing. $0.")
    elif age > 3 and age < 12:
        print("You have to pay $10.")
    elif age > 12:
        print("you have to pay $15.")
    else:
        break