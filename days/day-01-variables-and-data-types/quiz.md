# Day 1 Quiz: Variables and Data Types

## Questions

### 1. What is the difference between `int` and `float`?

**Your answer:**


**Correct answer:** `int` represents whole numbers (e.g., 42, -5, 0), while `float` represents decimal numbers (e.g., 3.14, -0.5, 2.0). Floats can represent fractional values, integers cannot.

---

### 2. How do you check the type of a variable?

**Your answer:**


**Correct answer:** Use the `type()` function. Example: `type(variable_name)`

---

### 3. What does the `//` operator do?

**Your answer:**


**Correct answer:** Floor division - divides and rounds down to the nearest integer. Example: `10 // 3` returns `3`, not `3.333...`

---

### 4. Can you add an integer and a string directly? Why or why not?

**Your answer:**


**Correct answer:** No, you cannot. Python doesn't automatically convert types in this case. You'll get a `TypeError`. You must explicitly convert one type to match the other: `str(5) + "hello"` or `5 + int("10")`

---

### 5. What's the output of `print(type(3.0))`?

**Your answer:**


**Correct answer:** `<class 'float'>` - Even though 3.0 looks like a whole number, the decimal point makes it a float.

---

## Score Yourself

- 5/5: Excellent! You understand the basics
- 3-4/5: Good! Review the concepts you missed
- 0-2/5: Review today's lesson and try again

## Next Steps

- If you scored 4-5: Move to Day 2
- If you scored 0-3: Review `README.md` and try exercises again
