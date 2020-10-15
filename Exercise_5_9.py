#no users:

usernames = ['aes','bes','ces','des','ees','admin']
if usernames != []:
    for user in usernames:
        if user == 'admin':
            print("Hello, admin! Would you like to see a status report?")
        else :
            print("hello",user,". Thank you for logging in.")
else :
    print("we need to find more users.")
