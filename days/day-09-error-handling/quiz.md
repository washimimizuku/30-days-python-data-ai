# Day 9 Quiz: Error Handling

## Questions

### 1. What is the purpose of try-except blocks?

**Your answer:**


**Correct answer:** Try-except blocks handle errors gracefully without crashing the program. Code in the `try` block is executed, and if an error occurs, the `except` block catches and handles it.

---

### 2. What's the difference between ValueError and TypeError?

**Your answer:**


**Correct answer:** ValueError occurs when a function receives the right type but inappropriate value (e.g., `int("abc")`). TypeError occurs when an operation is performed on an inappropriate type (e.g., `"text" + 5`).

---

### 3. When should you use a finally block?

**Your answer:**


**Correct answer:** Use `finally` for cleanup code that must run whether an exception occurred or not (e.g., closing files, releasing resources). It executes after try and except blocks.

---

### 4. How do you catch multiple exception types?

**Your answer:**


**Correct answer:** Use a tuple: `except (ValueError, TypeError) as e:` or use multiple except blocks for different handling of each type.

---

### 5. Why is catching all exceptions with bare `except:` considered bad practice?

**Your answer:**


**Correct answer:** It catches everything including system exits and keyboard interrupts, making debugging difficult and potentially hiding serious bugs. Always catch specific exceptions.

---

## Score Yourself
- 5/5: Excellent! - 3-4/5: Good! - 0-2/5: Review lesson

## Next Steps
- If you scored 4-5: Move to Day 10
- If you scored 0-3: Review `README.md`
