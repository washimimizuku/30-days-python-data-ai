# Day 19 Quiz: Working with CSV and JSON

## Questions

### 1. What's the difference between CSV and JSON formats?

**Your answer:**


**Correct answer:** CSV is a flat, tabular format (rows and columns) that's simple and compact. JSON is hierarchical, supports nested structures, and includes data types. CSV is better for simple tabular data, JSON for complex nested data.

---

### 2. How do you handle missing values when reading CSV?

**Your answer:**


**Correct answer:** Use `pd.read_csv(file, na_values=['', 'NA', 'null'])` to specify what values should be treated as missing. Pandas automatically recognizes common missing value indicators.

---

### 3. What does `orient='records'` do in `to_dict()`?

**Your answer:**


**Correct answer:** It converts a DataFrame to a list of dictionaries, where each dictionary represents a row with column names as keys. This format is ideal for JSON export.

---

### 4. How do you read a CSV file in chunks?

**Your answer:**


**Correct answer:** Use `pd.read_csv(file, chunksize=1000)` which returns an iterator. Process each chunk separately to handle files larger than memory.

---

### 5. Why might you choose JSON over CSV?

**Your answer:**


**Correct answer:** Choose JSON for nested/hierarchical data, when you need to preserve data types, for API communication, or when data structure is complex. CSV is better for simple tabular data and smaller file sizes.

---

## Score Yourself
- 5/5: Excellent! - 3-4/5: Good! - 0-2/5: Review

## Next Steps
- Move to Day 20: Mini Project - Data Analysis Tool
