import pandas as pd

data = {
    "Name": ["A", "B", "C", "D", "E"],
    "Age": [20, 25, 22, 30, 28],
    "Marks": [85, 72, 90, 65, 88],
    "City": ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai"]
}

df = pd.DataFrame(data)

# 1. First 3 rows
print("First 3 rows:")
print(df.head(3))

# 2. Last 2 rows
print("\nLast 2 rows:")
print(df.tail(2))

# 3. Shape
print("\nShape:", df.shape)

# 4. Column names
print("\nColumns:", df.columns.tolist())

# 5. Data types
print("\nData types:")
print(df.dtypes)

# 6. Select only Name and Marks
print("\nName and Marks:")
print(df[["Name", "Marks"]])

# 7. Students whose marks > 80
print("\nMarks > 80:")
print(df[df["Marks"] > 80])

# 8. Sort by marks highest to lowest
print("\nSorted by Marks (desc):")
print(df.sort_values("Marks", ascending=False))
