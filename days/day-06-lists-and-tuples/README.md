# Day 6: Lists and Tuples

## 📖 Learning Objectives (15 min)

- Create and manipulate lists
- Use list methods (append, insert, remove, pop)
- Understand tuples and immutability
- Slice sequences effectively

## Theory

### Lists
```python
# Create
numbers = [1, 2, 3, 4, 5]
mixed = [1, "two", 3.0, True]

# Access
first = numbers[0]      # 1
last = numbers[-1]      # 5

# Modify
numbers[0] = 10
numbers.append(6)       # Add to end
numbers.insert(0, 0)    # Insert at index
numbers.remove(3)       # Remove value
popped = numbers.pop()  # Remove and return last

# Slicing
numbers[1:4]   # [2, 3, 4]
numbers[:3]    # [1, 2, 3]
numbers[3:]    # [4, 5]
numbers[-2:]   # [4, 5]
numbers[::2]   # Every 2nd element
```

### Tuples (Immutable)
```python
coordinates = (10, 20)
rgb = (255, 128, 0)

# Access same as lists
x = coordinates[0]

# Cannot modify
# coordinates[0] = 15  # Error!

# Unpacking
x, y = coordinates
r, g, b = rgb
```

### List Methods
```python
numbers = [3, 1, 4, 1, 5]
numbers.sort()          # [1, 1, 3, 4, 5]
numbers.reverse()       # [5, 4, 3, 1, 1]
count = numbers.count(1)  # 2
index = numbers.index(4)  # 1
```

## 💻 Exercises (40 min)

Complete `exercise.py`

### Exercise 1: Sensor Reading Buffer
Manage a list of last 10 sensor readings

### Exercise 2: Data Filtering
Filter list based on conditions

### Exercise 3: Coordinate System
Use tuples for (x, y) coordinates

### Exercise 4: Data Pipeline
Process data through multiple steps

### Exercise 5: Time Series Data
Store and analyze time series in lists

## Tomorrow: Day 7 - Dictionaries and Sets
