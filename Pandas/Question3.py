import pandas as pd

data = {
    "Name": ["A", "B", "C", "D", "E", "F"],
    "Math": [80, 60, 90, 70, 85, 55],
    "Science": [75, 65, 95, 72, 80, 60],
    "English": [85, 70, 88, 75, 90, 50]
}

df = pd.DataFrame(data)

# 1. Create an Average column
df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)

# 2. Create a Total column
df["Total"] = df[["Math", "Science", "English"]].sum(axis=1)

# 3. Create a Passed column (Average >= 60 -> True)
df["Passed"] = df["Average"] >= 60

# 4. Student with the highest average
top = df.loc[df["Average"].idxmax()]
print("Highest average student:")
print(top)

# 5. Students whose average >= 80
print("\nAverage >= 80:")
print(df[df["Average"] >= 80])

# 6. Sort by average descending
print("\nSorted by Average (desc):")
print(df.sort_values("Average", ascending=False))

# 7. Overall average
print("\nOverall average:", df["Average"].mean())

# 8. Display only Name, Average, and Passed
print("\nName, Average, Passed:")
print(df[["Name", "Average", "Passed"]])
