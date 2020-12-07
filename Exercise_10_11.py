#Favorite Number:
import json

UserFavNumber = input("Please enter your favorite number:")

with open("Excercise_10_11.json",'w') as fileobject:
    json.dump(UserFavNumber,fileobject)
