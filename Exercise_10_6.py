#Addition:
FirstNumber = input("Please enter first number:")
SecondNumber = input("Please enter second number:")
try:
    FirstNumber = int(FirstNumber)
    SecondNumber = int(SecondNumber)
    print("Addition Result:",FirstNumber+SecondNumber)
except ValueError:
    print("Please enter a Number.")