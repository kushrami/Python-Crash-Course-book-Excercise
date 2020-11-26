#slices

list = []
for number in range(1,11):
    list.append(number**3)

print("first three element in list are",list[:3])
print("middle items are :",list[4:7])
print("last items are :",list[8:])
