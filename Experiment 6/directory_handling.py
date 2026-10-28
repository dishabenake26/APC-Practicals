
with open("student.txt", "w") as f:
    name = input("Enter your name: ")
    f.write(name)

print("Data written successfully")
################################################

with open("student.txt", "r") as f:
    data = f.read()

print("File contents:", data)
###############################################

with open("student.txt", "a") as f:
    text = input("Enter text to add: ")
    f.write("\n" + text)

print("Data added successfully")
################################################

with open("student.txt", "r") as f:
    for line in f:
        print(line, end="")
#############################################

with open("student.txt", "r") as f:
    data = f.read()

print("Characters:", len(data))
print("Words:", len(data.split()))
##############################################

with open("student.txt", "r") as f:
    lines = f.readlines()

print("Number of lines:", len(lines))
####################################################

with open("student.txt", "r") as f:
    data = f.read()

with open("copy.txt", "w") as f:
    f.write(data)

print("File copied successfully")
