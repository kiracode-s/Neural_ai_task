import pandas as pd

data = {
    "Age": [20, 21, None, 24, None, 30],
    "Salary": [30000, None, 40000, 50000, None, 60000],
    "Experience": [1, 2, 3, None, 5, 6],
    "Department": ["CS", "IT", "CS", None, "IT", "CS"]
}

df = pd.DataFrame(data)

# 1. Display the DataFrame
print("Original DataFrame:")
print(df)

# 2. Count missing values in every column
print("\nMissing values per column:")
print(df.isnull().sum())

# 3. Fill missing Age using the median
df["Age"] = df["Age"].fillna(df["Age"].median())

# 4. Fill missing Salary using the median
df["Salary"] = df["Salary"].fillna(df["Salary"].median())

# 5. Fill missing Experience using the median
df["Experience"] = df["Experience"].fillna(df["Experience"].median())

# 6. Fill missing Department using the mode
df["Department"] = df["Department"].fillna(df["Department"].mode()[0])

# 7. Verify no missing values
print("\nMissing values after filling:")
print(df.isnull().sum())

# 8. Print the cleaned DataFrame
print("\nCleaned DataFrame:")
print(df)
