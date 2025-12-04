# Day 14 Quiz: List Comprehensions

## Questions

### 1. What is the syntax for a basic list comprehension?

**Your answer:**


**Correct answer:** `[expression for item in iterable]` or with condition: `[expression for item in iterable if condition]`. Example: `[x*2 for x in range(5)]` creates `[0, 2, 4, 6, 8]`.

---

### 2. How do list comprehensions compare to regular loops?

**Your answer:**


**Correct answer:** List comprehensions are more concise, often faster, and more Pythonic. They're best for simple transformations. Use regular loops for complex logic or when you need multiple statements.

---

### 3. What's the difference between `[x for x in data]` and `(x for x in data)`?

**Your answer:**


**Correct answer:** Square brackets `[]` create a list comprehension (evaluates immediately, stores in memory). Parentheses `()` create a generator expression (lazy evaluation, memory efficient for large datasets).

---

### 4. Can you use multiple for clauses in a comprehension?

**Your answer:**


**Correct answer:** Yes! `[x*y for x in range(3) for y in range(3)]` creates nested loops. The order matters: later for clauses are nested inside earlier ones.

---

### 5. How do you create a dictionary comprehension?

**Your answer:**


**Correct answer:** Use curly braces with key:value pairs: `{key_expr: value_expr for item in iterable}`. Example: `{x: x**2 for x in range(5)}` creates `{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}`.

---

## Score Yourself
- 5/5: Excellent! - 3-4/5: Good! - 0-2/5: Review

## Next Steps
- Move to Day 15: NumPy Basics
