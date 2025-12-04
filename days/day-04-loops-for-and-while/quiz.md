# Day 4 Quiz: Loops

## Questions

### 1. What does `range(5)` produce?

**Your answer:**

**Correct answer:** Numbers 0, 1, 2, 3, 4 (5 numbers starting from 0, not including 5)

---

### 2. What's the difference between `break` and `continue`?

**Your answer:**

**Correct answer:** `break` exits the loop completely. `continue` skips the rest of the current iteration and moves to the next one.

---

### 3. How do you iterate over a list with indices?

**Your answer:**

**Correct answer:** Use `enumerate()`: `for index, value in enumerate(my_list):`

---

### 4. What's wrong with this code?
```python
for i in range(10):
    if i == 5:
        continue
    print(i)
    break
```

**Your answer:**

**Correct answer:** The `break` will execute on the first iteration (i=0), so it only prints 0 and exits. The `continue` on i==5 never matters.

---

### 5. How do you create a countdown from 10 to 1?

**Your answer:**

**Correct answer:** `for i in range(10, 0, -1):` - start at 10, stop before 0, step by -1

---

## Score: ___/5
