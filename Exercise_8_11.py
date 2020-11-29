#Unchanged Magicians:

listOfMagicians = ['Dynamo','david blain','karan singh magic']
newListOfMagicians = []

def show_magicians(listOfMagicians):
    for magician in listOfMagicians:
        print(magician)

def make_great(listofnames):
    for name in listofnames:
        newListOfMagicians.append("The Great "+name)


show_magicians(listOfMagicians)
make_great(listOfMagicians)
show_magicians(newListOfMagicians)