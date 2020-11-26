#Shrinking guests list:

names = ['tony','steve','thor']

message = ", You are invited!"
attendeemessage = " is not coming."

print(str(len(names))+" People are invited.")
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
print("so total of "+str(len(names))+" people are invited")
print("New table will not be available on time. So only two people will be invited.")

notinvitedmsg = ", You are not invited."
print(names[5]+notinvitedmsg)
names.pop(5)
print(names[4]+notinvitedmsg)
names.pop(4)
print(names[3]+notinvitedmsg)
names.pop(3)
print(names[2]+notinvitedmsg)
names.pop(2)
print("so total of "+str(len(names))+" people are invited")
print(names[0]+message)
print(names[1]+message)

names.remove('tony')
del names[0]
print(names)
