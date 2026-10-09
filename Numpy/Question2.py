import numpy as np

X = np.array([
    [10, 100, 1000],
    [20, 200, 2000],
    [30, 300, 3000],
    [40, 400, 4000],
    [50, 500, 5000]
])

# 1. Mean of each column
mean = np.mean(X, axis=0)
print("Column means:", mean)

# 2. Standard deviation of each column
std = np.std(X, axis=0)
print("Column stds:", std)

# 3. Standardize using broadcasting (no loops)
X_scaled = (X - mean) / std

# 4. Print the scaled matrix
print("\nScaled matrix:")
print(X_scaled)

# 5. Verify: mean ≈ 0 and std ≈ 1 for each scaled column
print("\nVerification:")
print("Scaled column means:", np.mean(X_scaled, axis=0))
print("Scaled column stds:", np.std(X_scaled, axis=0))
