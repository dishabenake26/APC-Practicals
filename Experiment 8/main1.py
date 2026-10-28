from Student_Package.info import detail
from Student_Package.marks import calculate_percentage, calculate_grade

name, age, course, year = detail("Disha", 21, "CSE", "3rd")

print("_____Student Detail______\n")
print("Name:", name)
print("Age:", age)
print("Course:", course)
print("Year:", year)

percentage = calculate_percentage(450, 500)
grade = calculate_grade(percentage)

print("Percentage:", percentage)
print("Grade:", grade)