#Summing a million:
list = []
for number in range(1,1000001):
    list.append(number)

print(min(list))
print(max(list))
print("python doing sum of 1 million = ",sum(list))
