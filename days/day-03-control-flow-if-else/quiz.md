# Day 3 Quiz: Control Flow

## Questions

### 1. What's wrong with this code?
```python
if x > 10:
print("Big")
```

**Your answer:**

**Correct answer:** Missing indentation. Python uses indentation to define code blocks. Should be:
```python
if x > 10:
    print("Big")
```

---

### 2. What's the output if score = 75?
```python
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
```

**Your answer:**

**Correct answer:** "C" - The elif conditions are checked in order, and 75 >= 70 is True.

---

### 3. What does this ternary operator do?
```python
result = "even" if x % 2 == 0 else "odd"
```

**Your answer:**

**Correct answer:** It assigns "even" to result if x is even, otherwise assigns "odd". It's a shorthand for if-else.

---

### 4. When do you need elif instead of multiple if statements?

**Your answer:**

**Correct answer:** Use elif when conditions are mutually exclusive and you want to check them in order. Once one condition is True, the rest are skipped. Multiple if statements check all conditions regardless.

---

### 5. What's the difference between `and` and nested if?
```python
# Version 1
if age >= 18 and has_license:
    print("Can drive")

# Version 2
if age >= 18:
    if has_license:
        print("Can drive")
```

**Your answer:**

**Correct answer:** They produce the same result, but nested if is more verbose. Use `and` for simple conditions, nested if when you need different actions at each level.

---

## Score: ___/5
