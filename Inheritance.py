#Single Inheritance
class mother:
    fav_dish="Puran Poli"

class child(mother):
    fav_breverage="Cold Coffee"

c=child()

print("Favourite Dish:",c.fav_dish)
print("Favourite Breverage:",c.fav_breverage)
#######################################################
#Multiple Inheritance
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




