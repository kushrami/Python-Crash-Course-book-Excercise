#Learning C:
with open('learning_python.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    line = line.replace('python','C')
    print(line)
print(lines)