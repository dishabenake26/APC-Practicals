
def add(a, b):
    return a + b

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

result = add(x, y)

print("Sum:", result)
####################################################

def check(num):
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

n = int(input("Enter a number: "))
check(n)
#############################################

def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact

n = int(input("Enter a number: "))
print("Factorial:", factorial(n))
######################################################

def largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

print("Largest number:", largest(x, y, z))
###################################################

def area(radius):
    return 3.14 * radius * radius

r = float(input("Enter radius: "))

print("Area of circle:", area(r))
##################################################

def prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

num = int(input("Enter a number: "))

if prime(num):
    print("Prime number")
else:
    print("Not a prime number")
