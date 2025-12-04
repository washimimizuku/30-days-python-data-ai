# Day 18 Quiz: Pandas Grouping and Aggregation

## Questions

### 1. What does groupby() do in pandas?

**Your answer:**


**Correct answer:** `groupby()` splits data into groups based on one or more columns, allowing you to perform operations on each group separately. It follows the split-apply-combine pattern.

---

### 2. How do you apply multiple aggregation functions to grouped data?

**Your answer:**


**Correct answer:** Use `.agg()` with a dictionary mapping columns to lists of functions: `df.groupby('col').agg({'col1': ['sum', 'mean'], 'col2': ['min', 'max']})`.

---

### 3. What's the difference between transform() and apply() in groupby?

**Your answer:**


**Correct answer:** `transform()` returns a Series with the same shape as the original (broadcasts result back), while `apply()` can return any shape and is more flexible but slower.

---

### 4. How do you create a pivot table in pandas?

**Your answer:**


**Correct answer:** Use `pd.pivot_table(df, values='value_col', index='row_col', columns='col_col', aggfunc='sum')`. It reshapes data from long to wide format with aggregation.

---

### 5. When would you use groupby vs pivot_table?

**Your answer:**


**Correct answer:** Use `groupby()` for flexible aggregations and when you want to keep data in long format. Use `pivot_table()` when you need to reshape data into a cross-tabulation format for easier viewing.

---

## Score Yourself
- 5/5: Excellent! - 3-4/5: Good! - 0-2/5: Review

## Next Steps
- Move to Day 19: Working with CSV and JSON
