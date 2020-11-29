#sandwiches:

def orderedsandwich(items):
    list_of_items = []
    for item in items:
        list_of_items.append(item)
    print("This is items you ordered in your sandwich:")
    for item in list_of_items:
        print(item)

orderedsandwich(['kela','aloo'])
orderedsandwich(['cheese','poteto'])
orderedsandwich(['uiyer'])