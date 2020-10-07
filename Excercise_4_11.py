#My pizzas, your pizzas:

mypizzas = ['margerita','thincrust','peripiri']
friend_pizzas = mypizzas[:]
mypizzas.append('cheese')
friend_pizzas.append('burst')

print("so like, i love pizza. My favorite pizzas are :")
for pizza in mypizzas:
    print(pizza)

print("Tony's pizzas are :")
for pizza in friend_pizzas:
    print(pizza)


