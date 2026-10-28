
class Dog:
    def sound(self):
        print("Dog barks")

class Cat:
    def sound(self):
        print("Cat meows")

d = Dog()
c = Cat()

d.sound()
c.sound()
#################################################333


class Parent:
    def display(self):
        print("Parent class method")

class Child(Parent):
    def display(self):
        print("Child class method")

c = Child()
c.display()
