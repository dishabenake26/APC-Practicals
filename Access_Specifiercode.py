class Animal:

    # Public variable
    name = "Animal"

    # Protected variable
    _age = 5

    # Private variable
    __color = "White"

    # Public function
    def eat(self):
        print("Animal eats")

    # Protected function
    def _sleep(self):
        print("Animal sleeps")

    # Private function
    def __sound(self):
        print("Animal makes sound")

    # Function to access private members
    def show_private(self):
        print("Private variable:", self.__color)
        self.__sound()


class Dog(Animal):

    def bark(self):
        print("Dog barks")

    def show_details(self):
        # Public member
        print("Public variable:", self.name)

        # Protected member
        print("Protected variable:", self._age)
        self._sleep()

        # Private member of Animal
        # self.__color       # Cannot access directly
        # self.__sound()     # Cannot access directly


class Puppy(Dog):

    def play(self):
        print("Puppy plays")

    def show_details_puppy(self):
        print("Public variable:", self.name)
        print("Protected variable:", self._age)

        self.eat()       # Public function
        self._sleep()    # Protected function

        # Private members cannot be directly accessed
        # self.__color
        # self.__sound()


# Object of Puppy
p = Puppy()

print("----- PUBLIC -----")
print(p.name)
p.eat()

print("\n----- PROTECTED -----")
print(p._age)
p._sleep()

print("\n----- PRIVATE -----")
p.show_private()

print("\n----- INHERITANCE -----")
p.bark()
p.play()