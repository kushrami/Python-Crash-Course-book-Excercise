#Guest Book:

while True:
    User_name = input("Please enter your name or enter 'q' to exit:")
    if User_name == 'q':
        break
    else:
        with open('guest_book.txt','a') as file_object:
            file_object.write(User_name)
            file_object.write('\n')
        print("You can check your name in file guest_book.txt")
    