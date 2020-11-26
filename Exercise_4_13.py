#Buffet

Buffet_tuple = ('tea','coffee','snacks','bread','hotdog')
print("Hotel offers:")
for items in Buffet_tuple:
    print(items)

Buffet_tuple[0] = 'greentea'
print("Now on Hotel offers:")
Buffet_tuple = ('greentea','blackcoffee','snacks')
for items in Buffet_tuple:
    print(items)
