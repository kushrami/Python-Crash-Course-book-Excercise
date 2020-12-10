#Population:
def CityCountryFunc(city, country, population=0):
    if population:
        return str(city)+', '+str(country)+',population - '+str(population)
    else:
        return str(city)+', '+str(country)

