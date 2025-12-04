# Day 2 Quiz: Operators and Expressions

## Questions

### 1. What does `10 < x < 20` check in Python?

**Your answer:**

**Correct answer:** It checks if x is between 10 and 20 (exclusive). Python allows chaining comparisons, which is equivalent to `10 < x and x < 20`.

---

### 2. What is the result of `True and False or True`?

**Your answer:**

**Correct answer:** `True`. Due to operator precedence, `and` is evaluated before `or`, so it's `(True and False) or True` = `False or True` = `True`.

---

### 3. How do you check if a number is even?

**Your answer:**

**Correct answer:** Use the modulo operator: `number % 2 == 0`. If the remainder when divided by 2 is 0, the number is even.

---

### 4. What's the difference between `=` and `==`?

**Your answer:**

**Correct answer:** `=` is assignment (assigns a value to a variable), while `==` is comparison (checks if two values are equal and returns True/False).

---

### 5. What does `not (x > 10 and x < 20)` mean?

**Your answer:**

**Correct answer:** It checks if x is NOT between 10 and 20. It's true when x is <= 10 or x >= 20.

---

## Score: ___/5
