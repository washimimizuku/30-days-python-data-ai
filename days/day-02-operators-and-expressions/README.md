# Day 2: Operators and Expressions

## 📖 Learning Objectives (15 min)

- Master comparison operators
- Understand logical operators (and, or, not)
- Learn operator precedence
- Work with boolean expressions

---

## Theory

### Comparison Operators

```python
x = 10
y = 5

x == y   # Equal: False
x != y   # Not equal: True
x > y    # Greater than: True
x < y    # Less than: False
x >= y   # Greater or equal: True
x <= y   # Less or equal: False
```

### Logical Operators

```python
# AND - both must be True
True and True    # True
True and False   # False

# OR - at least one must be True
True or False    # True
False or False   # False

# NOT - opposite
not True         # False
not False        # True
```

### Combining Operators

```python
age = 25
has_license = True

# Can drive if age >= 18 AND has license
can_drive = age >= 18 and has_license  # True

# Discount if age < 18 OR age > 65
gets_discount = age < 18 or age > 65   # False
```

### Operator Precedence

Order (highest to lowest):
1. `**` (exponentiation)
2. `*`, `/`, `//`, `%` (multiplication, division)
3. `+`, `-` (addition, subtraction)
4. `==`, `!=`, `<`, `>`, `<=`, `>=` (comparison)
5. `not`
6. `and`
7. `or`

```python
# Use parentheses for clarity
result = (10 + 5) * 2  # 30
result = 10 + 5 * 2    # 20
```

### Chaining Comparisons

```python
x = 15
# Check if x is between 10 and 20
10 < x < 20  # True (Python allows this!)

# Equivalent to:
10 < x and x < 20
```

---

## 💻 Exercises (40 min)

Complete `exercise.py`

### Exercise 1: Age Checker
Check if someone can:
- Vote (age >= 18)
- Drink alcohol (age >= 21)
- Retire (age >= 65)

### Exercise 2: Temperature Classifier
Classify temperature as:
- Freezing (< 0)
- Cold (0-15)
- Moderate (16-25)
- Hot (> 25)

### Exercise 3: Data Validation
Validate user data:
- Username: 3-20 characters
- Age: 0-120
- Email: contains "@"

### Exercise 4: Logical Combinations
Determine if a number is:
- Even AND positive
- Divisible by 3 OR 5
- NOT in range 10-20

### Exercise 5: Data Quality Check
Check if data point is valid:
- Temperature: -50 to 50
- Humidity: 0 to 100
- Pressure: 900 to 1100
- All values present (not None)

---

## ✅ Quiz (5 min)

See `quiz.md`

---

## 🎯 Key Takeaways

- Comparison operators return boolean values
- Logical operators combine boolean expressions
- Use parentheses for complex expressions
- Python allows chaining comparisons
- Operator precedence matters

---

## Tomorrow: Day 3 - Control Flow (if/else)
