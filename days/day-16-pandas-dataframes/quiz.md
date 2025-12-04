# Day 16 Quiz: Pandas DataFrames

## Questions

### 1. What's the difference between loc and iloc?

**Your answer:**


**Correct answer:** `loc` uses label-based indexing (row/column names), while `iloc` uses integer position-based indexing. Example: `df.loc[0, 'name']` vs `df.iloc[0, 0]`.

---

### 2. How do you select multiple columns from a DataFrame?

**Your answer:**


**Correct answer:** Use double brackets with a list of column names: `df[['col1', 'col2']]`. Single brackets `df['col1']` returns a Series, double brackets returns a DataFrame.

---

### 3. What does `df.describe()` do?

**Your answer:**


**Correct answer:** Returns statistical summary (count, mean, std, min, quartiles, max) for numerical columns. It's useful for quick data exploration and understanding distributions.

---

### 4. How do you filter rows where age > 25 AND city is 'NYC'?

**Your answer:**


**Correct answer:** Use `df[(df['age'] > 25) & (df['city'] == 'NYC')]`. Note: use `&` for AND, `|` for OR, and parentheses around each condition.

---

### 5. What's the difference between a DataFrame and a Series?

**Your answer:**


**Correct answer:** A DataFrame is a 2D table with rows and columns (like a spreadsheet). A Series is a 1D array (single column). A DataFrame is essentially a collection of Series.

---

## Score Yourself
- 5/5: Excellent! - 3-4/5: Good! - 0-2/5: Review

## Next Steps
- Move to Day 17: Pandas Data Cleaning
