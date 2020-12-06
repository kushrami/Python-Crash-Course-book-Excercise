#Programming Poll:
while True:
    User_name = input("Why do you like programming? or enter 'q' to exit:")
    if User_name == 'q':
        break
    else:
        with open('Programming_poll.txt','a') as file_object:
            file_object.write(User_name)
            file_object.write('\n')