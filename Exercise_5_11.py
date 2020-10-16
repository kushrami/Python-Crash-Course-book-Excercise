#ordinal numbers:
list = []
for i in range(1,10):
    list.append(i)

for number in list:
    if number == 1:
        print("Ordinal number 1st")
    elif number == 2:
        print("Ordinal Number 2nd")
    elif number == 3:
        print("Ordinal number 3rd")
    else:
        print("Not Ordinal number "+str(number)+"th")