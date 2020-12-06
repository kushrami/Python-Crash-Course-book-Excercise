#Addition Calculator:

ExitFlag = True


while ExitFlag:
    
    FirstNumber = input("Please enter first number or 'q' to exit:")
    if FirstNumber == 'q':
        break
    else:
        SecondNumber = input("Please enter second number or 'q' to exit:")
        if SecondNumber == 'q':
            break
        else:
            try:
                FirstNumber = int(FirstNumber)
                SecondNumber = int(SecondNumber)
                print("Addition Result:",FirstNumber+SecondNumber)
            except ValueError:
                print("Please enter a Number.")