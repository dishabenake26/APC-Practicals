
from array import array

numbers = array('i')

n = int(input("How many numbers? "))

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

print("Array:", numbers)

from array import array

numbers = array('i', [10, 20, 30, 40])

print("Original array:", numbers)

numbers.insert(1, 15)
print("After insertion:", numbers)

numbers.remove(30)
print("After removal:", numbers)

from array import array

numbers = array('i', [10, 20, 30, 40, 50])

total = sum(numbers)

print("Array:", numbers)
print("Sum:", total)
