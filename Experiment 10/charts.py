
import matplotlib.pyplot as plt
# Data
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

# 1. Line Graph
plt.plot(x, y, color='red', marker='o')
plt.title("Line Graph")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()

# 2. Bar Graph
plt.bar(x, y, color='skyblue')
plt.title("Bar Graph")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()

# 3. Scatter Plot
plt.scatter(x, y, color='green')
plt.title("Scatter Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()

# 4. Pie Chart
labels = ['Python', 'Java', 'C++', 'C']
sizes = [40, 30, 20, 10]

plt.pie(
    sizes,
    labels=labels,
    autopct='%1.1f%%',
    colors=['orange', 'pink', 'lightgreen', 'violet']
)
plt.title("Pie Chart")
plt.show()

# 5. Histogram
marks = [45, 50, 55, 60, 65, 70, 70, 75, 80, 85, 90, 95]

plt.hist(marks, bins=5, color='purple', edgecolor='black')
plt.title("Histogram")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

# 6. Horizontal Bar Graph
plt.barh(x, y, color='coral')
plt.title("Horizontal Bar Graph")
plt.xlabel("Y Values")
plt.ylabel("X Values")
plt.show()
