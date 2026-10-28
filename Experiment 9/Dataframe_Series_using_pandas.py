
import pandas as pd

# Create Dataset
data = {
    'Name': ['Amit', 'Priya', 'Rahul', 'Sneha', 'Riya'],
    'Age': [20, 21, 19, None, 22],
    'Marks': [85, 90, 78, 88, None],
    'City': ['Pune', 'Mumbai', 'Pune', 'Delhi', 'Mumbai']
}

df = pd.DataFrame(data)

# 1. Display Dataset
print("Dataset:")
print(df)

# 2. Display First 5 Rows
print("\nFirst 5 Rows:")
print(df.head())

# 3. Display Last 5 Rows
print("\nLast 5 Rows:")
print(df.tail())

# 4. Display Dataset Information
print("\nDataset Information:")
df.info()

# 5. Statistical Summary
print("\nStatistical Summary:")
print(df.describe())

# 6. Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# 7. Handle Missing Values
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Marks'] = df['Marks'].fillna(df['Marks'].mean())
print("\nAfter Handling Missing Values:")
print(df)

# 8. Display Dataset Shape
print("\nDataset Shape:")
print(df.shape)

# 9. Display Column Names
print("\nColumn Names:")
print(df.columns)

# 10. Select a Column
print("\nStudent Names:")
print(df['Name'])

# 11. Filter Students with Marks Above 80
print("\nStudents with Marks Above 80:")
print(df[df['Marks'] > 80])

# 12. Sort by Marks
print("\nSorted by Marks:")
print(df.sort_values(by='Marks', ascending=False))

# 13. Find Average Marks
print("\nAverage Marks:")
print(df['Marks'].mean())

# 14. Group by City
print("\nAverage Marks by City:")
print(df.groupby('City')['Marks'].mean())

# 15. Save Dataset to CSV
df.to_csv('students.csv', index=False)
print("\nDataset saved successfully!")