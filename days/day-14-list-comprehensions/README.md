# Day 14: List Comprehensions

## 📖 Learning Objectives (15 min)

- Master list comprehension syntax
- Use comprehensions for filtering and transformation
- Create dictionary and set comprehensions
- Understand when to use comprehensions vs loops
- Write readable, Pythonic code

---

## Theory

### Basic List Comprehension

**Traditional Loop:**
```python
squares = []
for x in range(10):
    squares.append(x**2)
```

**List Comprehension:**
```python
squares = [x**2 for x in range(10)]
```

**Syntax:**
```python
[expression for item in iterable]
```

### With Condition (Filtering)

```python
# Only even numbers
evens = [x for x in range(20) if x % 2 == 0]

# Only positive numbers
positives = [x for x in [-2, -1, 0, 1, 2] if x > 0]

# Squares of even numbers
even_squares = [x**2 for x in range(10) if x % 2 == 0]
```

### Transforming Data

```python
# Convert to uppercase
names = ["alice", "bob", "charlie"]
upper_names = [name.upper() for name in names]

# Extract specific fields
users = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}]
names = [user["name"] for user in users]

# Temperature conversion
celsius = [0, 10, 20, 30, 40]
fahrenheit = [c * 9/5 + 32 for c in celsius]
```

### Nested Comprehensions

```python
# Flatten 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
# Result: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Create multiplication table
table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
```

### Dictionary Comprehensions

```python
# Create dictionary
squares_dict = {x: x**2 for x in range(5)}
# Result: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Invert dictionary
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
# Result: {1: 'a', 2: 'b', 3: 'c'}

# Filter dictionary
data = {"a": 1, "b": 2, "c": 3, "d": 4}
filtered = {k: v for k, v in data.items() if v > 2}
# Result: {'c': 3, 'd': 4}
```

### Set Comprehensions

```python
# Unique squares
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_squares = {x**2 for x in numbers}
# Result: {1, 4, 9, 16}

# Unique lengths
words = ["hello", "world", "hi", "python"]
lengths = {len(word) for word in words}
# Result: {2, 5, 6}
```

### When to Use Comprehensions

**✅ Use comprehensions when:**
- Simple transformation or filtering
- One-liner makes code clearer
- Creating new list/dict/set from existing data

**❌ Use regular loops when:**
- Complex logic with multiple statements
- Need to handle exceptions
- Logic is hard to read in one line
- Side effects (printing, file I/O)

---

## 💻 Exercises (40 min)

Complete `exercise.py`

### Exercise 1: Basic Transformations
Create lists using comprehensions for various transformations

### Exercise 2: Filtering Data
Filter sensor readings based on conditions

### Exercise 3: Dictionary Operations
Create and transform dictionaries

### Exercise 4: Nested Data
Work with nested structures

### Exercise 5: Real-World Data Processing
Process sensor data using comprehensions

---

## ✅ Quiz (5 min)

See `quiz.md`

---

## 🎯 Key Takeaways

- List comprehensions are more concise than loops
- Syntax: `[expression for item in iterable if condition]`
- Works for lists, dictionaries, and sets
- Use for simple transformations, loops for complex logic
- Comprehensions are Pythonic and often faster

---

## Tomorrow: Day 15 - NumPy Basics

We'll learn about NumPy arrays for efficient numerical computing.
