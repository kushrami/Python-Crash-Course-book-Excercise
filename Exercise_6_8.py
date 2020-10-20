#Pets:

cat ={
    'kind' : 'wierd',
    'owner' : 'tony',
}

dog = {
    'kind' : 'loyal',
    'owner' : 'steve',
}

lion = {
    'kind' : 'heavy',
    'owner' : 'thor',
}

tiger = {
    'kind' : 'dangerous',
    'owner' : 'T\'Challa',
}

pets = [cat,dog,lion,tiger]
for pet in pets:
    print("Detailes of pet:")
    for keys,values in pet.items():
        print(keys,":",values)
