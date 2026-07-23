a=10
b=-100
print(type(a))
print(type(b))

PI=23.89
Sci=456.90
print(type(PI))
print(type(Sci))

z=3+5j
print(type(z))
print(z.conjugate())

name="Disha Benake"
print(type(name))
print(name[2::4])

n="hello"
print(bool(n))
print(bool(1))
print(bool(0))

value = "123" #string
num = int(value)#conversion of string to int
print(num + 10)  


numbers = [10, 20, 30]
print(type(numbers))

data = (10, 20, 30)
print(type(data))

r = range(5)
print(list(r))
print(type(r))


student = {
    "name":"Disha",
    "age":20,
    "passion":"doctor",
    "roll":25
}

print(type(student))
print(student.keys())
print(student.values())


s = {1,2,3,4}
print(type(s))
fs = frozenset([1,2,3])
print(type(fs))
