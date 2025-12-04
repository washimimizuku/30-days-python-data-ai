# Day 15 Quiz: NumPy Basics

## Questions

### 1. What is the main advantage of NumPy arrays over Python lists?

**Your answer:**


**Correct answer:** NumPy arrays are faster and more memory-efficient for numerical operations. They support vectorized operations (element-wise operations without loops), have a fixed type, and provide many mathematical functions.

---

### 2. What does "broadcasting" mean in NumPy?

**Your answer:**


**Correct answer:** Broadcasting allows NumPy to perform operations on arrays of different shapes by automatically expanding smaller arrays to match larger ones. Example: adding a scalar to an array adds it to every element.

---

### 3. How do you access the element in row 2, column 3 of a 2D array?

**Your answer:**


**Correct answer:** Use `array[2, 3]` (note: 0-indexed, so this is the 3rd row, 4th column). You can also use `array[2][3]` but the comma notation is preferred and more efficient.

---

### 4. What's the difference between `np.array([1,2,3])` and `np.array([[1,2,3]])`?

**Your answer:**


**Correct answer:** The first creates a 1D array with shape `(3,)`. The second creates a 2D array with shape `(1, 3)` - a row vector. The extra brackets add a dimension.

---

### 5. How do you filter an array to get only values greater than 5?

**Your answer:**


**Correct answer:** Use boolean indexing: `arr[arr > 5]`. This creates a boolean mask and returns only elements where the condition is True.

---

## Score Yourself
- 5/5: Excellent! - 3-4/5: Good! - 0-2/5: Review

## Next Steps
- Move to Day 16: Pandas DataFrames
