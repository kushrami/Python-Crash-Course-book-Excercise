#Rivers:

state_rivers = {
    'gujarat' : 'narmada',
    'delhi' : 'ganga',
    'karnataka' : 'kaveri'
}

for state,river in state_rivers.items():
    print("The river "+river+" run through "+state+".")
for river in state_rivers.values():
    print("The river "+river+" is amazing.")
for state in state_rivers.keys():
    print("The state "+state+" is amazing.")