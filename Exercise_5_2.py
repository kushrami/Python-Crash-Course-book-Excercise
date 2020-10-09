#more conditional test:

car = 'ferrari'
print(car == 'ferrari')
print(car == 'tesla')
print(car != 'tesla')
print(car != 'ferrari')
print(car == car.lower())
print(car == car.upper())

print(3 > 9)
print(3 < 9)
print(4 >= 5)
print(4 <= 4)
print(4 > 4)
print(3 <= 7)
print(6 < 7)

print((3 > 4) or (3 < 4))
print((4 >= 3) and (car == 'ferrari'))
print((6 < 9) or (4 == 5))
print((car != 'tesla') and (4 > 3))

list = ['car','truck']
if 'ferrari' in list:
    print(True)
if 'car' in list:
    print("is it ferrari?",car == 'ferrari')

if 'bike' not in list:
    list.append('bike')
    print("Is bike is added in list?",'bike' == list[2])