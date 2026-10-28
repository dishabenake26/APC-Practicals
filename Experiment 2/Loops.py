n = int(input("Enter n: "))

for i in range(1, n + 1):
    print(i)

#########################################
n = int(input("Enter n: "))

for i in range(2, n + 1, 2):
    print(i)
#########################################3
n = int(input("Enter n: "))

for i in range(1, n + 1, 2):
    print(i)
################################
n = int(input("Enter number of terms: "))

value = 1

for i in range(n):
    print(value, end=" ")
    value *= 2
############################################
n = int(input("Enter n: "))

fact = 1
sum = 1

for i in range(1, n + 1):
    fact *= i
    sum += 1 / fact

print("Sum =", sum)
#############################################33
x = float(input("Enter x (in radians): "))
n = int(input("Enter number of terms: "))

sum = 1
sign = -1
fact = 1

for i in range(2, 2 * n + 1, 2):
    fact = 1
    for j in range(1, i + 1):
        fact *= j

    sum += sign * (x ** i) / fact
    sign *= -1

print("cos(x) =", sum)
###########################################33333
import math

num = int(input("Enter number: "))

root = int(math.sqrt(num))

prime = True

if root < 2:
    prime = False
else:
    for i in range(2, root):
        if root % i == 0:
            prime = False
            break

print("Square root =", root)

if prime:
    print("Square root is Prime")
else:
    print("Square root is Not Prime")
#################################################3333
for i in range(3):
    print("ABC")
############################################
n = int(input("Enter n: "))

for i in range(1, n + 1):
    for j in range(i):
        print(chr(65 + j), end="")
    print()
####################################################3333
n = int(input("Enter n: "))

for i in range(n, 0, -1):
    for j in range(i):
        print(chr(65 + j), end="")
    print()
##########################################################33333333
n = int(input("Enter n: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
##########################################################3333333
n = int(input("Enter n: "))

for i in range(1, n + 1):
    for j in range(i):
        print(i, end="")
    print()
#############################################################3333333