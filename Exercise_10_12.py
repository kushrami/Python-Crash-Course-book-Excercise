#Favorite Number remembered:

import json
try:
    with open("Excercise_10_11.json") as fileobject:
        number = json.load(fileobject)
    print("Your favorite number is : ",number)
except:
    UserFavNumber = input("Please enter your favorite number:")

    with open("Excercise_10_11.json",'w') as fileobject:
        json.dump(UserFavNumber,fileobject)

    with open("Excercise_10_11.json") as fileobject:
        number = json.load(fileobject)
    print("Your favorite number is : ",number)

