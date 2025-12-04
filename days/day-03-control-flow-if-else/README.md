# Day 3: Control Flow - if/else Statements

## 📖 Learning Objectives (15 min)

- Use if, elif, else statements
- Write nested conditionals
- Understand indentation in Python
- Make decisions in code

---

## Theory

### Basic if Statement

```python
age = 20

if age >= 18:
    print("You are an adult")
```

### if-else

```python
temperature = 15

if temperature > 20:
    print("It's warm")
else:
    print("It's cold")
```

### if-elif-else

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
```

### Nested if Statements

```python
age = 25
has_license = True

if age >= 18:
    if has_license:
        print("Can drive")
    else:
        print("Need license")
else:
    print("Too young")
```

### Ternary Operator

```python
# Short form
status = "adult" if age >= 18 else "minor"

# Equivalent to:
if age >= 18:
    status = "adult"
else:
    status = "minor"
```

---

## 💻 Exercises (40 min)

Complete `exercise.py`

### Exercise 1: Grade Calculator
Convert numeric score to letter grade (A-F)

### Exercise 2: Temperature Advisor
Give clothing advice based on temperature

### Exercise 3: Data Validator
Validate and categorize data points

### Exercise 4: Anomaly Detector
Detect anomalies in sensor data

### Exercise 5: User Access Control
Determine user permissions based on role and status

---

## ✅ Quiz (5 min)

See `quiz.md`

---

## Tomorrow: Day 4 - Loops (for and while)
