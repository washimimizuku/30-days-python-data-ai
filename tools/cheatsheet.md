# Python Quick Reference Cheatsheet
*For 30 Days of Python for Data and AI*

## Variables & Data Types

```python
# Variables
name = "Alice"
age = 25
height = 1.75
is_student = True

# Check type
type(name)  # <class 'str'>

# Type conversion
int("42")      # String to int
float("3.14")  # String to float
str(42)        # Int to string
```

## Operators

```python
# Arithmetic
10 + 5   # Addition: 15
10 - 5   # Subtraction: 5
10 * 5   # Multiplication: 50
10 / 5   # Division: 2.0
10 // 3  # Floor division: 3
10 % 3   # Modulo: 1
2 ** 3   # Exponentiation: 8

# Comparison
==  # Equal
!=  # Not equal
<   # Less than
>   # Greater than
<=  # Less than or equal
>=  # Greater than or equal

# Logical
and  # Both true
or   # At least one true
not  # Opposite
```

## Strings

```python
# Creation
s = "Hello"
s = 'Hello'
s = """Multi
line"""

# Operations
"Hello" + " World"  # Concatenation
"Ha" * 3           # Repetition: "HaHaHa"
len("Hello")       # Length: 5

# F-strings (Python 3.6+)
name = "Alice"
f"Hello, {name}!"  # "Hello, Alice!"

# Methods
s.upper()          # "HELLO"
s.lower()          # "hello"
s.strip()          # Remove whitespace
s.split(",")       # Split into list
s.replace("a", "b") # Replace characters
```

## Lists

```python
# Creation
numbers = [1, 2, 3, 4, 5]
mixed = [1, "two", 3.0, True]

# Access
numbers[0]         # First: 1
numbers[-1]        # Last: 5
numbers[1:3]       # Slice: [2, 3]

# Methods
numbers.append(6)  # Add to end
numbers.insert(0, 0)  # Insert at index
numbers.remove(3)  # Remove value
numbers.pop()      # Remove and return last
len(numbers)       # Length
```

## Tuples (Immutable)

```python
# Creation
coords = (10, 20)
rgb = (255, 128, 0)

# Access (same as lists)
coords[0]          # 10

# Unpacking
x, y = coords
r, g, b = rgb

# Cannot modify
# coords[0] = 15   # Error!
```

## Sets (Unique Values)

```python
# Creation
unique = {1, 2, 3, 3, 4}  # {1, 2, 3, 4}

# Operations
unique.add(5)      # Add element
unique.remove(1)   # Remove element

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}
a | b              # Union: {1, 2, 3, 4, 5}
a & b              # Intersection: {3}
a - b              # Difference: {1, 2}
```

## Dictionaries

```python
# Creation
person = {
    "name": "Alice",
    "age": 25,
    "city": "NYC"
}

# Access
person["name"]     # "Alice"
person.get("age")  # 25

# Methods
person.keys()      # dict_keys(['name', 'age', 'city'])
person.values()    # dict_values(['Alice', 25, 'NYC'])
person.items()     # Key-value pairs
```

## Control Flow

```python
# If-else
if condition:
    # code
elif other_condition:
    # code
else:
    # code

# For loop
for item in iterable:
    # code

# While loop
while condition:
    # code

# Break and continue
for i in range(10):
    if i == 5:
        break      # Exit loop
    if i % 2 == 0:
        continue   # Skip to next iteration
```

## Functions

```python
# Definition
def greet(name):
    return f"Hello, {name}!"

# With default arguments
def greet(name="World"):
    return f"Hello, {name}!"

# Multiple returns
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers)

# Call
result = greet("Alice")
```

## File I/O

```python
# Read file
with open("file.txt", "r") as f:
    content = f.read()

# Write file
with open("file.txt", "w") as f:
    f.write("Hello, World!")

# Read lines
with open("file.txt", "r") as f:
    for line in f:
        print(line.strip())
```

## List Comprehensions

```python
# Basic
squares = [x**2 for x in range(10)]

# With condition
evens = [x for x in range(10) if x % 2 == 0]

# Nested
matrix = [[i*j for j in range(3)] for i in range(3)]
```

## Common Patterns

```python
# Range
range(5)           # 0, 1, 2, 3, 4
range(1, 6)        # 1, 2, 3, 4, 5
range(0, 10, 2)    # 0, 2, 4, 6, 8

# Enumerate
for i, value in enumerate(['a', 'b', 'c']):
    print(i, value)  # 0 a, 1 b, 2 c

# Zip
for x, y in zip([1, 2, 3], ['a', 'b', 'c']):
    print(x, y)  # 1 a, 2 b, 3 c

# Try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

## NumPy Basics

```python
import numpy as np

# Create array
arr = np.array([1, 2, 3, 4, 5])

# Operations
arr + 10           # Add to all elements
arr * 2            # Multiply all elements
arr.mean()         # Average
arr.sum()          # Sum
arr.max()          # Maximum
```

## Pandas Basics

```python
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35]
})

# Access
df['name']         # Column
df.iloc[0]         # Row by index
df.loc[0, 'name']  # Specific cell

# Operations
df.head()          # First 5 rows
df.describe()      # Statistics
df.groupby('age').mean()  # Group by
df[df['age'] > 25] # Filter
```

## Object-Oriented Programming

```python
# Class definition
class Sensor:
    def __init__(self, sensor_id, location):
        self.sensor_id = sensor_id
        self.location = location
    
    def read(self):
        return f"Reading from {self.sensor_id}"

# Create instance
sensor = Sensor(101, "Building A")
sensor.read()

# Inheritance
class SmartSensor(Sensor):
    def __init__(self, sensor_id, location, wifi):
        super().__init__(sensor_id, location)
        self.wifi = wifi
```

## Error Handling

```python
# Try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError as e:
    print(f"Value error: {e}")
finally:
    print("Always runs")

# Multiple exceptions
try:
    # code
except (ValueError, TypeError) as e:
    print(f"Error: {e}")
```

## Modules and Imports

```python
# Import module
import math
math.sqrt(16)      # 4.0

# Import specific function
from math import sqrt, pi
sqrt(16)           # 4.0

# Import with alias
import pandas as pd
import numpy as np

# Import your own module
import my_module
from my_module import my_function
```

## DateTime

```python
from datetime import datetime, timedelta

# Current time
now = datetime.now()

# Create specific datetime
dt = datetime(2024, 1, 15, 14, 30)

# Arithmetic
tomorrow = now + timedelta(days=1)
last_week = now - timedelta(weeks=1)

# Formatting
now.strftime("%Y-%m-%d")           # "2024-01-15"
now.strftime("%B %d, %Y")          # "January 15, 2024"

# Parsing
dt = datetime.strptime("2024-01-15", "%Y-%m-%d")
```

## Regular Expressions

```python
import re

# Search
match = re.search(r'\d+', 'Order 12345')  # Finds '12345'

# Find all
numbers = re.findall(r'\d+', 'Call 555-1234')

# Replace
text = re.sub(r'\d+', 'X', 'Room 123')  # 'Room X'

# Common patterns
r'\d'      # Digit
r'\w'      # Word character
r'\s'      # Whitespace
r'.'       # Any character
r'+'       # One or more
r'*'       # Zero or more
r'{3}'     # Exactly 3
```

## Working with APIs

```python
import requests

# GET request
response = requests.get('https://api.example.com/data')
if response.status_code == 200:
    data = response.json()

# POST request
data = {'name': 'Alice', 'age': 25}
response = requests.post('https://api.example.com/users', json=data)

# With parameters
params = {'q': 'python', 'limit': 10}
response = requests.get('https://api.example.com/search', params=params)
```

## Async Programming

```python
import asyncio

# Define async function
async def fetch_data(id):
    await asyncio.sleep(1)  # Simulate I/O
    return f"Data {id}"

# Run async function
result = asyncio.run(fetch_data(1))

# Run multiple concurrently
async def main():
    results = await asyncio.gather(
        fetch_data(1),
        fetch_data(2),
        fetch_data(3)
    )
    return results

asyncio.run(main())
```

## Type Hints

```python
# Basic types
def greet(name: str) -> str:
    return f"Hello, {name}"

def add(a: int, b: int) -> int:
    return a + b

# Complex types
from typing import List, Dict, Optional

def process(data: List[float], 
            config: Dict[str, any],
            threshold: Optional[float] = None) -> List[float]:
    pass
```

## Testing with pytest

```python
# test_calculator.py
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

# Run: pytest test_calculator.py

# With fixtures
import pytest

@pytest.fixture
def sample_data():
    return [1, 2, 3, 4, 5]

def test_sum(sample_data):
    assert sum(sample_data) == 15
```

## Matplotlib Basics

```python
import matplotlib.pyplot as plt

# Line plot
plt.plot(x, y)
plt.title('My Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

# Scatter plot
plt.scatter(x, y, c=colors, s=sizes)
plt.colorbar()
plt.show()

# Subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
axes[0, 0].plot(x, y)
axes[0, 1].scatter(x, y)
plt.tight_layout()
plt.show()

# Save figure
plt.savefig('plot.png', dpi=300)
```

## Virtual Environments

```bash
# Create virtual environment
python -m venv venv

# Activate
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# Install packages
pip install pandas numpy

# Save requirements
pip freeze > requirements.txt

# Install from requirements
pip install -r requirements.txt

# Deactivate
deactivate
```

## Common Pandas Operations

```python
import pandas as pd

# Read/Write
df = pd.read_csv('data.csv')
df.to_csv('output.csv', index=False)

# Data cleaning
df.dropna()                    # Remove missing
df.fillna(0)                   # Fill missing
df.drop_duplicates()           # Remove duplicates

# Filtering
df[df['age'] > 25]             # Filter rows
df[(df['age'] > 25) & (df['city'] == 'NYC')]

# Grouping
df.groupby('category').mean()
df.groupby('category').agg({'value': ['mean', 'sum']})

# Sorting
df.sort_values('age')
df.sort_values(['city', 'age'], ascending=[True, False])
```

## Tips & Best Practices

**General:**
- Use meaningful variable names
- Follow PEP 8 style guide
- Comment your code
- Use f-strings for formatting

**Data Structures:**
- Use lists for ordered, mutable data
- Use tuples for immutable data
- Use sets for unique values
- Use dicts for key-value pairs

**Functions:**
- Keep functions small and focused
- Use type hints for clarity
- Return early to avoid nesting

**Error Handling:**
- Catch specific exceptions
- Use try-except for expected errors
- Always clean up resources (use `with`)

**Performance:**
- Use list comprehensions when readable
- Use NumPy for numerical operations
- Use pandas for data manipulation
- Avoid loops when vectorization possible

**Testing:**
- Write tests for critical functions
- Test edge cases
- Use fixtures for reusable test data

---

**Quick Links:**
- [Python Docs](https://docs.python.org/3/)
- [NumPy Docs](https://numpy.org/doc/)
- [Pandas Docs](https://pandas.pydata.org/docs/)
- [Matplotlib Docs](https://matplotlib.org/)
