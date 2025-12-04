# Day 11: Modules and Imports

## 📖 Learning Objectives (15 min)
- Import and use modules
- Create your own modules
- Understand `__name__ == "__main__"`
- Use common standard library modules

## Theory

### Importing Modules
```python
# Import entire module
import math
result = math.sqrt(16)

# Import specific functions
from math import sqrt, pi
result = sqrt(16)

# Import with alias
import pandas as pd
df = pd.DataFrame()

# Import all (not recommended)
from math import *
```

### Creating Modules
```python
# mymodule.py
def greet(name):
    return f"Hello, {name}!"

PI = 3.14159

# main.py
import mymodule
print(mymodule.greet("Alice"))
```

### Standard Library
```python
import os          # Operating system
import sys         # System-specific
import datetime    # Date and time
import random      # Random numbers
import json        # JSON handling
import re          # Regular expressions
```

## 💻 Exercises (40 min)

### Exercise 1: Use Standard Library
Work with os, datetime, random modules

### Exercise 2: Create Data Utils Module
Build reusable data processing functions

### Exercise 3: Import Patterns
Practice different import styles

### Exercise 4: Module Organization
Organize code into multiple modules

### Exercise 5: Package Structure
Create a simple package with __init__.py

## Tomorrow: Day 12 - Object-Oriented Programming
