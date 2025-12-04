"""
Day 15: NumPy Basics - Solutions
"""

import numpy as np

# Exercise 1
array_from_list = np.array([1, 2, 3, 4, 5])
zeros_array = np.zeros(5)
ones_array = np.ones(5)
range_array = np.arange(0, 10, 2)
random_array = np.random.rand(5)

print("Exercise 1:")
print(f"From list: {array_from_list}")
print(f"Zeros: {zeros_array}")
print(f"Ones: {ones_array}")
print(f"Range: {range_array}")
print(f"Random: {random_array}")
print()

# Exercise 2
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([10, 20, 30, 40, 50])

print("Exercise 2:")
print(f"arr1: {arr1}")
print(f"arr2: {arr2}")
print(f"Add: {arr1 + arr2}")
print(f"Subtract: {arr2 - arr1}")
print(f"Multiply: {arr1 * arr2}")
print(f"Divide: {arr2 / arr1}")
print(f"Power: {arr1 ** 2}")
print()

# Exercise 3
data = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

print("Exercise 3:")
print(f"Data: {data}")
print(f"First element: {data[0]}")
print(f"Last element: {data[-1]}")
print(f"First 3: {data[:3]}")
print(f"Last 3: {data[-3:]}")
print(f"Every 2nd: {data[::2]}")
print(f"Reverse: {data[::-1]}")
print()

# Exercise 4
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("Exercise 4:")
print(f"Matrix:\n{matrix}")
print(f"Shape: {matrix.shape}")
print(f"First row: {matrix[0]}")
print(f"First column: {matrix[:, 0]}")
print(f"Element [1,1]: {matrix[1, 1]}")
print(f"2x2 submatrix:\n{matrix[:2, :2]}")
print()

# Exercise 5
sensor_data = np.array([23.5, 24.1, 23.8, 25.0, 24.5, 26.2, 25.8, 24.9])

print("Exercise 5:")
print(f"Sensor data: {sensor_data}")
print(f"Mean: {np.mean(sensor_data):.2f}")
print(f"Median: {np.median(sensor_data):.2f}")
print(f"Std Dev: {np.std(sensor_data):.2f}")
print(f"Min: {np.min(sensor_data):.2f}")
print(f"Max: {np.max(sensor_data):.2f}")
print(f"Sum: {np.sum(sensor_data):.2f}")
print()

# Bonus: Broadcasting and advanced operations
print("Bonus:")

# Broadcasting: add scalar to array
temps_celsius = np.array([20, 25, 30])
temps_kelvin = temps_celsius + 273.15
print(f"Celsius: {temps_celsius}")
print(f"Kelvin: {temps_kelvin}")

# Boolean indexing
data = np.array([23.5, 26.1, 24.8, 27.3, 22.9, 28.1, 25.5])
hot_temps = data[data > 25]
print(f"\nAll temps: {data}")
print(f"Hot temps (>25): {hot_temps}")

# Reshaping
arr = np.arange(12)
reshaped = arr.reshape(3, 4)
print(f"\nOriginal: {arr}")
print(f"Reshaped (3x4):\n{reshaped}")

# Matrix operations
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(f"\nMatrix A:\n{A}")
print(f"Matrix B:\n{B}")
print(f"Matrix multiplication:\n{np.dot(A, B)}")
print(f"Transpose of A:\n{A.T}")
