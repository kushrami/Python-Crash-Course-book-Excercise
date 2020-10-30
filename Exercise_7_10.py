#Dream vacation:

listOfPoll = []
Flag = True
while Flag:
    user_place = input("What's that one place you want to go, if not intrested then type 'q':")
    if user_place == 'q':
        Flag = False
        print("Polling result",listOfPoll)
    else:
        print("That place is amazing. Thank you for Polling")
        listOfPoll.append(user_place)