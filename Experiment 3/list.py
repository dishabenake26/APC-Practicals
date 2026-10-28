
numbers = []

n = int(input("How many numbers? "))

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

print("List:", numbers)

numbers = [10, 20, 30]

print("Original list:", numbers)

num = int(input("Enter number to add: "))
numbers.append(num)

print("Updated list:", numbers)

numbers = [12, 45, 7, 23, 9]

print("List:", numbers)
print("Largest number:", max(numbers))
print("Smallest number:", min(numbers))

numbers = [10, 20, 30, 40, 50]

n = int(input("Enter number to search: "))

if n in numbers:
    print("Number found")
else:
    print("Number not found")

numbers = [40, 10, 30, 20, 50]

print("Original list:", numbers)

numbers.sort()

print("Sorted list:", numbers)
