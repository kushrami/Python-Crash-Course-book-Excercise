#silent Cats and dogs:
try:
    with open('cat.txt') as fileobject:
        content = fileobject.read()
        print(content)
    with open('dog.txt') as fileobject:
        content = fileobject.read()
        print(content)
except FileNotFoundError:
    pass


