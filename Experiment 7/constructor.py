
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

name = input("Enter name: ")
age = int(input("Enter age: "))

s1 = Student(name, age)
s1.display()
