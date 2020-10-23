#Multiple of ten:

number_of_ten = input("Please enter a number to check whether its multiple of 10 or not:")

if (int(number_of_ten) % 10) == 0:
    print("Yes, your",number_of_ten,"is multiple of ten.")
else:
    print("No, your",number_of_ten,"is not multiple of ten.")