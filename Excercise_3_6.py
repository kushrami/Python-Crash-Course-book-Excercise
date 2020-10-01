#More guests:

names = ['tony','steve','thor']

message = ", You are invited!"
attendeemessage = " is not coming."

print(names[0]+message)
print(names[1]+message)
print(names[2]+message)

print(names[1]+attendeemessage)
del names[1]
names.insert(1,'peter')
print(names[0]+message)
print(names[1]+message)
print(names[2]+message)

print("Ok, We found new table for booking.")
names.insert(0,'jessi')
names.insert(3,'laura')
names.append('sandy')
print(names[0]+message)
print(names[1]+message)
print(names[2]+message)
print(names[3]+message)
print(names[4]+message)
print(names[5]+message)

