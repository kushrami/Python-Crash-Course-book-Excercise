#Polling:

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
    
List_of_people = ['jen','sarah','edward','tony','thor','phil']

for person in List_of_people:
    if person in favorite_languages.keys():
        print("Thank you for polling,",person)
    else:
        print("Please take poll,",person)