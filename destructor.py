class Student:

    # Constructor
    def __init__(self):
        print("Constructor is called")

    # Destructor
    def __del__(self):
        print("Destructor is called")


s1 = Student()

del s1