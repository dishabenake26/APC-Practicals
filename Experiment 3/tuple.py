
values = input("Enter values separated by spaces: ").split()

data = tuple(values)

print("Tuple:", data)
print("Length:", len(data))

numbers = (10, 20, 30, 40, 50)

print("First element:", numbers[0])
print("Last element:", numbers[-1])
print("Tuple:", numbers)

numbers = (10, 20, 10, 30, 10, 40)

n = int(input("Enter number to count: "))

print("Count:", numbers.count(n))

numbers = (15, 8, 42, 23, 5)

print("Tuple:", numbers)
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
