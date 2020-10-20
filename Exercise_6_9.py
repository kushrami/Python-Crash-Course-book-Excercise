#Favorite Places:

favorite_places = {
    'tony': ['newyork','delhi','paris'],
    'thor': ['asgard','newyork','austin'],
    'nessa': ['huawai','tokyo','mumbai'],
}

for keys,values in favorite_places.items():
    print("The favorite places of",keys,"is:")
    for value in values:
        print(value)    