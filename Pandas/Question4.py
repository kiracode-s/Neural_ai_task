import pandas as pd

data = {
    "Employee": ["A", "B", "C", "D", "E", "F", "G", "H"],
    "Department": ["CS", "CS", "IT", "IT", "CS", "IT", "HR", "HR"],
    "Salary": [50000, 60000, 55000, 65000, 70000, 75000, 40000, 45000],
    "Experience": [2, 4, 3, 5, 6, 7, 1, 2]
}

df = pd.DataFrame(data)

grouped = df.groupby("Department")

# 1. Average salary per department
print("Average salary per department:")
print(grouped["Salary"].mean())

# 2. Maximum salary per department
print("\nMax salary per department:")
print(grouped["Salary"].max())

# 3. Minimum salary per department
print("\nMin salary per department:")
print(grouped["Salary"].min())

# 4. Average experience per department
print("\nAverage experience per department:")
print(grouped["Experience"].mean())

# 5. Department with the highest average salary
avg_salary = grouped["Salary"].mean()
print("\nDepartment with highest avg salary:", avg_salary.idxmax(), "->", avg_salary.max())

# 6. Count employees in each department
print("\nEmployee count per department:")
print(grouped["Employee"].count())

# 7. Sort departments by average salary
print("\nDepartments sorted by avg salary:")
print(avg_salary.sort_values(ascending=False))