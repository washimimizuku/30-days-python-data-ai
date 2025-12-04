# Day 8 Quiz: File I/O

## Questions

### 1. Why should you use the `with` statement when working with files?

**Your answer:**


**Correct answer:** The `with` statement automatically closes the file when done, even if an error occurs. This prevents resource leaks and ensures proper file handling. It's a context manager that handles cleanup automatically.

---

### 2. What's the difference between "w" and "a" modes?

**Your answer:**


**Correct answer:** "w" (write) mode overwrites the entire file if it exists, or creates a new file. "a" (append) mode adds content to the end of an existing file without deleting existing content, or creates a new file if it doesn't exist.

---

### 3. How do you read a file line by line efficiently?

**Your answer:**


**Correct answer:** Iterate directly over the file object: `for line in f:`. This is memory-efficient as it reads one line at a time, unlike `readlines()` which loads the entire file into memory.

---

### 4. What does `newline=""` do in CSV writing?

**Your answer:**


**Correct answer:** It prevents extra blank lines in CSV files on Windows. The CSV module handles line endings itself, so `newline=""` tells Python not to add additional line ending translation.

---

### 5. How do you check if a file exists before opening it?

**Your answer:**


**Correct answer:** Use `os.path.exists(filename)` or `pathlib.Path(filename).exists()`. This returns True if the file exists, False otherwise.

---

## Score Yourself

- 5/5: Excellent! You understand file I/O
- 3-4/5: Good! Review the concepts you missed
- 0-2/5: Review today's lesson and try exercises again

## Next Steps

- If you scored 4-5: Move to Day 9
- If you scored 0-3: Review `README.md` and try exercises again
