
student = {}

student["name"] = input("Enter student name: ")
student["roll_no"] = input("Enter roll number: ")
student["city"] = input("Enter city: ")

print("Student details:", student)
#############################################

student = {"name": "Amit", "age": 20}

print("Original dictionary:", student)

student["city"] = "Pune"
print("After adding city:", student)

student["age"] = 21
print("After updating age:", student)
######################################################

student = {"name": "Amit", "age": 20, "city": "Pune"}

key = input("Enter key to search: ")

if key in student:
    print("Value:", student[key])
else:
    print("Key not found")
###########################################

student = {
    "name": "Disha",
    "age": 21,
    "city": "Kolhapur"
}

for key, value in student.items():
    print(key, ":", value)
##################################################

student = {"name": "Amit", "age": 20, "city": "Pune"}

print("Original dictionary:", student)

key = input("Enter key to delete: ")

if key in student:
    del student[key]
    print("Updated dictionary:", student)
else:
    print("Key not found")
