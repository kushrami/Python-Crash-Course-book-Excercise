#checking usernames:

current_users = ['aes','bes','ces','des','ees','admin']
new_users = ['Ees','mes','les','kes']

for user in new_users:
        if user.lower() in current_users:
            print("Please enter new user name.")
        else :
            print("hello",user,". Username is available.")
