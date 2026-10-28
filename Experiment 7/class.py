
class Student:
    def display(self):
        print("Welcome to Python programming")

s1 = Student()
s1.display()
####################################################33

class Student:
    def get_data(self):
        self.name = input("Enter student name: ")
        self.roll = int(input("Enter roll number: "))

    def display(self):
        print("Name:", self.name)
        print("Roll number:", self.roll)

s1 = Student()
s1.get_data()
s1.display()
