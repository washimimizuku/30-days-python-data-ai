# Day 17 Quiz: Pandas Data Cleaning

## Questions

### 1. What's the difference between fillna() and dropna()?

**Your answer:**


**Correct answer:** `fillna()` replaces missing values with specified values (mean, median, forward fill, etc.). `dropna()` removes rows or columns containing missing values. Use fillna() to preserve data, dropna() when missing data is not recoverable.

---

### 2. How do you detect outliers using the IQR method?

**Your answer:**


**Correct answer:** Calculate Q1 (25th percentile), Q3 (75th percentile), and IQR = Q3 - Q1. Outliers are values < Q1 - 1.5*IQR or > Q3 + 1.5*IQR. This is the same method used in box plots.

---

### 3. What does `pd.to_numeric(series, errors='coerce')` do?

**Your answer:**


**Correct answer:** Converts a series to numeric type. The `errors='coerce'` parameter converts invalid values to NaN instead of raising an error. Useful for cleaning data with mixed types.

---

### 4. How do you remove duplicate rows?

**Your answer:**


**Correct answer:** Use `df.drop_duplicates()`. By default, it keeps the first occurrence. Use `keep='last'` to keep the last, or `keep=False` to remove all duplicates. Can specify `subset` to check specific columns.

---

### 5. What's the purpose of method chaining in pandas?

**Your answer:**


**Correct answer:** Method chaining allows multiple operations in sequence without intermediate variables, making code more readable and concise. Example: `df.fillna(0).drop_duplicates().sort_values('col')`.

---

## Score Yourself
- 5/5: Excellent! - 3-4/5: Good! - 0-2/5: Review

## Next Steps
- Move to Day 18: Pandas Grouping and Aggregation
