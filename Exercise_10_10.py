#Common Words:

with open('gutenberg.txt') as fileobject:
    content = fileobject.read()

thecount = content.lower().count('the')
print(thecount)