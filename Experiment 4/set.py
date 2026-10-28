
values = input("Enter numbers separated by spaces: ").split()

numbers = set(values)

print("Set:", numbers)
print("Number of elements:", len(numbers))
###################################################

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Set A:", a)
print("Set B:", b)
print("Union:", a.union(b))
print("Intersection:", a.intersection(b))
##################################################

a = {10, 20, 30, 40}
b = {30, 40, 50, 60}

print("A - B:", a - b)
print("B - A:", b - a)
###########################################

numbers = {10, 20, 30}

print("Original set:", numbers)

n = int(input("Enter number to add: "))
numbers.add(n)
print("After adding:", numbers)

n = int(input("Enter number to remove: "))
numbers.discard(n)
print("After removing:", numbers)
#############################################