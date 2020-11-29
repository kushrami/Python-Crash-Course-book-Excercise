#Great magician:

listOfMagicians = ['Dynamo','david blain','karan singh magic']

def show_magicians(listOfMagicians):
    for magician in listOfMagicians:
        print(magician)

def make_great(name):
    listOfMagicians.remove(name)
    listOfMagicians.append("The GREAT "+name)

show_magicians(listOfMagicians)
make_great('Dynamo')
show_magicians(listOfMagicians)