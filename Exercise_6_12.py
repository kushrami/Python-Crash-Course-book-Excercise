#Extensions:

# I have Taken Example 5.9 and extended it to dictionary
#no users:

usernames = {
    'aes':{
        'password':'64545465',
        'key' : '56' 
    },
    'bes':{
        'password':'64545465',
        'key' : '56' 
    },
    'ces':{
        'password':'64546545',
        'key' : '56' 
    },
    'admin':{
        'password':'64546465',
        'key' : '5' 
    }
}
if usernames != {}:
    for user,info in usernames.items():
        if user == 'admin':
            print("Hello, admin! here are all the username and password")
            print(usernames)            

        else :
            print("hello",user,". Thank you for logging in.")
            for password,key in info.items():
                print(password,":",key)
else :
    print("we need to find more users.")
