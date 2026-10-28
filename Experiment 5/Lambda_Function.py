
square = lambda x: x * x

n = int(input("Enter a number: "))

print("Square:", square(n))
###########################################

add = lambda a, b: a + b

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Sum:", add(x, y))
#################################################

largest = lambda a, b: a if a > b else b

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Largest number:", largest(x, y))
##########################################

cube = lambda x: x * x * x

n = int(input("Enter a number: "))

print("Cube:", cube(n))
