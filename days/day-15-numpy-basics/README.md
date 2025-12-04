# Day 15: NumPy Basics - Arrays

## 📖 Learning Objectives (15 min)

- Understand NumPy arrays and their advantages
- Create and manipulate arrays
- Perform vectorized operations
- Use array indexing and slicing
- Apply mathematical operations efficiently

---

## Theory

### Why NumPy?

NumPy (Numerical Python) is fundamental for data science:
- **Fast**: 10-100x faster than Python lists
- **Memory efficient**: Uses less memory
- **Vectorized operations**: No loops needed
- **Foundation**: Pandas, scikit-learn built on NumPy

### Creating Arrays

```python
import numpy as np

# From list
arr = np.array([1, 2, 3, 4, 5])

# Zeros and ones
zeros = np.zeros(5)          # [0. 0. 0. 0. 0.]
ones = np.ones((3, 4))       # 3x4 array of ones

# Range
arr = np.arange(0, 10, 2)    # [0, 2, 4, 6, 8]
arr = np.linspace(0, 1, 5)   # 5 values from 0 to 1

# Random
random = np.random.rand(5)   # 5 random values [0, 1)
random_int = np.random.randint(0, 10, 5)  # 5 random integers
```

### Array Operations (Vectorized)

```python
arr = np.array([1, 2, 3, 4, 5])

# Arithmetic (element-wise)
arr + 10        # [11, 12, 13, 14, 15]
arr * 2         # [2, 4, 6, 8, 10]
arr ** 2        # [1, 4, 9, 16, 25]

# Array operations
arr1 = np.array([1, 2, 3])
arr2 = np.array([10, 20, 30])
arr1 + arr2     # [11, 22, 33]
arr1 * arr2     # [10, 40, 90]
```

### Indexing and Slicing

```python
arr = np.array([10, 20, 30, 40, 50])

arr[0]          # 10 (first element)
arr[-1]         # 50 (last element)
arr[1:4]        # [20, 30, 40]
arr[::2]        # [10, 30, 50] (every 2nd)

# Boolean indexing
arr[arr > 25]   # [30, 40, 50]
```

### 2D Arrays (Matrices)

```python
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

matrix.shape    # (3, 3)
matrix[0, 0]    # 1 (row 0, col 0)
matrix[0]       # [1, 2, 3] (first row)
matrix[:, 0]    # [1, 4, 7] (first column)
matrix[:2, :2]  # [[1, 2], [4, 5]] (submatrix)
```

### Statistical Operations

```python
arr = np.array([23.5, 24.1, 23.8, 25.0, 24.5])

np.mean(arr)    # 24.18
np.median(arr)  # 24.1
np.std(arr)     # 0.54
np.min(arr)     # 23.5
np.max(arr)     # 25.0
np.sum(arr)     # 120.9
```

### Reshaping

```python
arr = np.arange(12)         # [0, 1, 2, ..., 11]
reshaped = arr.reshape(3, 4)  # 3x4 matrix

# Flatten
flat = reshaped.flatten()   # Back to 1D
```

---

## 💻 Exercises (40 min)

Complete `exercise.py`

### Exercise 1: Array Creation
Create arrays using different methods

### Exercise 2: Array Operations
Perform vectorized operations

### Exercise 3: Indexing and Slicing
Practice array access patterns

### Exercise 4: 2D Arrays
Work with matrices

### Exercise 5: Sensor Data Analysis
Analyze sensor data with NumPy

---

## Tomorrow: Day 16 - Pandas DataFrames
