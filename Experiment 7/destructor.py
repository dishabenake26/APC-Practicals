
class Demo:
    def __init__(self):
        print("Object created")

    def __del__(self):
        print("Object destroyed")

d1 = Demo()
del d1
