#people:

person_0 = {
    'firstname' : 'Tony',
    'lastname' : 'stark',
    'age' : 32,
    'city' : 'newyork'
    }
person_1 = {
    'firstname' : 'steve',
    'lastname' : 'rogers',
    'age' : 132,
    'city' : 'queens'
    }
person_2 = {
    'firstname' : 'thor',
    'lastname' : 'sone of odin',
    'age' : 1032,
    'city' : 'asgard'
    }

list_of_person = [person_0,person_1,person_2]

for person in list_of_person:
    print("Details of Person:")
    for keys,info in person.items():
        print(keys,":",info)