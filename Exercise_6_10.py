#favorite numbers:

PeopleFavNumbers ={
    'tony' : [4,34],
    'thor' : [5],
    'steve' : [7,56,90],
    'peter' : [6,789,78],
    'nessa' : [8,93,63]
}

for name,numbers in PeopleFavNumbers.items():
    print("Favorite numbers of "+name+" is :")
    for number in numbers:
        print(number)