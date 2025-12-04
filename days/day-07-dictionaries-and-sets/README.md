# Day 7: Dictionaries and Sets

## 📖 Learning Objectives (15 min)
- Create and use dictionaries
- Access and modify dictionary data
- Use sets for unique values
- Choose appropriate data structures

## Theory

### Dictionaries
```python
# Create
user = {"name": "Alice", "age": 25, "city": "NYC"}

# Access
name = user["name"]
age = user.get("age", 0)  # With default

# Modify
user["email"] = "alice@example.com"
user["age"] = 26

# Methods
keys = user.keys()
values = user.values()
items = user.items()

# Iterate
for key, value in user.items():
    print(f"{key}: {value}")
```

### Sets
```python
# Create
unique_ids = {1, 2, 3, 3, 4}  # {1, 2, 3, 4}
empty_set = set()

# Operations
unique_ids.add(5)
unique_ids.remove(1)
unique_ids.discard(10)  # No error if not found

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}
union = a | b        # {1, 2, 3, 4, 5}
intersection = a & b  # {3}
difference = a - b    # {1, 2}
```

## 💻 Exercises (40 min)

### Exercise 1: User Data Management
Store and manage user information in dictionaries

### Exercise 2: Word Frequency Counter
Count word occurrences in text

### Exercise 3: Remove Duplicates
Use sets to find unique values

### Exercise 4: Data Lookup System
Build fast lookup with dictionaries

### Exercise 5: Configuration Manager
Manage app configuration with nested dictionaries

## Tomorrow: Day 8 - File I/O
