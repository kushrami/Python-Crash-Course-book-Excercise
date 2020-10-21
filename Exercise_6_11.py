#cites:

cites = {
    'mumbai': {
        'country': 'india',
        'population' : 110_000_000,
        'fact' : 'every area is divided in two parts, east & west'
    },
    'newyork':{
        'country': 'US',
        'population' : 51_000_000,
        'fact' : 'everyone is so freaking busy.'
    },
}

for cityname,details in cites.items():
    print("Here are some details about",cityname)
    for detail,value in details.items():
        print(detail,":",value) 