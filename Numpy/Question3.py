import numpy as np

X = np.array([
    [25, 50000],
    [17, 30000],
    [35, 80000],
    [42, 90000],
    [19, 25000],
    [31, 70000]
])

# 1. People whose age >= 25
age_mask = X[:, 0] >= 25
print("Age >= 25:")
print(X[age_mask])

# 2. People whose salary > 60000
salary_mask = X[:, 1] > 60000
print("\nSalary > 60000:")
print(X[salary_mask])

# 3. Age >= 25 AND salary > 60000
both_mask = age_mask & salary_mask
print("\nAge >= 25 AND Salary > 60000:")
print(X[both_mask])

# 4. Replace salaries below 30000 with 30000
X[X[:, 1] < 30000, 1] = 30000
print("\nAfter replacing salaries < 30000:")
print(X)

# 5. Average salary (all)
print("\nAverage salary:", np.mean(X[:, 1]))

# 6. Average salary only for people aged >= 25
print("Average salary (age >= 25):", np.mean(X[X[:, 0] >= 25, 1]))
