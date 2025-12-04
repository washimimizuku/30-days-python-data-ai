# Day 9: Error Handling

## 📖 Learning Objectives (15 min)
- Use try-except blocks
- Handle specific exceptions
- Use finally clause
- Raise custom exceptions

## Theory

### Basic Try-Except
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

### Multiple Exceptions
```python
try:
    value = int(input("Enter number: "))
    result = 10 / value
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print(f"Unexpected error: {e}")
```

### Finally Clause
```python
try:
    f = open("file.txt")
    data = f.read()
except FileNotFoundError:
    print("File not found")
finally:
    f.close()  # Always executes
```

### Raising Exceptions
```python
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 120:
        raise ValueError("Age too high")
    return age
```

## 💻 Exercises (40 min)

### Exercise 1: Safe Calculator
Division with error handling

### Exercise 2: File Reader
Read files with proper error handling

### Exercise 3: Data Validator
Validate data and raise appropriate exceptions

### Exercise 4: Retry Logic
Implement retry mechanism for operations

### Exercise 5: Custom Exceptions
Create custom exception classes

## Tomorrow: Day 10 - Mini Project
