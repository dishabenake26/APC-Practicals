# #Single Inheritance
class mother:
    fav_dish="Puran Poli"

class child(mother):
    fav_breverage="Cold Coffee"

c=child()

print("Favourite Dish:",c.fav_dish)
print("Favourite Breverage:",c.fav_breverage)

# #######################################################
# #Multiple Inheritance
class kingdom:
    n1="Animalia"
class phylum:
    n2="Chordata"
class genes:
    n3="Canis"
class species(kingdom,phylum,genes):
    n4="Canis lupus familiaris"
p=species()

print("Kingdom:",p.n1)
print("Phylum:",p.n2)
print("Genes:",p.n3)
print("Species:",p.n4)
#######################################
#Multiltvel Inheritance
class Animal:
    def eat(self):
        print("Animal eats")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Dog):
    def mammal(self):
        print("These both are mammals")

m = Cat()

print("\n____Feature of Animals____\n")

m.eat()
m.bark()
m.mammal()
#######################################
#Hierarchial Inheritance
class Employee:

    name = "Disha"

    def work(self):
        print("Employee is working")


class Manager(Employee):

    def manage(self):
        print("Manager manages the team")


class Developer(Employee):

    def code(self):
        print("Developer writes code")


m = Manager()
d = Developer()

print("Manager:")
print("Name:", m.name)
m.work()
m.manage()

print("\nDeveloper:")
print("Name:", d.name)
d.work()
d.code()
# ########################################

#Hybrid Inheritance

class Person:

    name = "Disha"

    def introduce(self):
        print("I am a person")


class Student(Person):

    college = "ABC College"

    def study(self):
        print("Student studies")


class Employee(Person):

    company = "XYZ Company"

    def work(self):
        print("Employee works")


class Intern(Student, Employee):

    duration = 6

    def training(self):
        print("Intern is doing training")


i = Intern()

print("Name:", i.name)
print("College:", i.college)
print("Company:", i.company)
print("Duration:", i.duration)

i.introduce()
i.study()
i.work()
i.training()





