# Day 5: Functions and Scope

## 📖 Learning Objectives (15 min)
- Define and call functions
- Use parameters and return values
- Understand scope (local vs global)
- Use default arguments

## Theory

### Basic Function
```python
def greet(name):
    return f"Hello, {name}!"

result = greet("Alice")  # "Hello, Alice!"
```

### Parameters and Returns
```python
def add(a, b):
    return a + b

def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers)/len(numbers)

minimum, maximum, average = get_stats([1, 2, 3, 4, 5])
```

### Default Arguments
```python
def power(base, exponent=2):
    return base ** exponent

power(5)      # 25 (uses default exponent=2)
power(5, 3)   # 125
```

### Scope
```python
x = 10  # Global

def my_function():
    y = 5  # Local
    print(x)  # Can access global
    print(y)  # Can access local

# print(y)  # Error! y is local to function
```

## 💻 Exercises (40 min)

### Exercise 1: Calculator Functions
Create add, subtract, multiply, divide functions

### Exercise 2: Data Validator
Function to validate data ranges

### Exercise 3: Temperature Converter
celsius_to_fahrenheit() and fahrenheit_to_celsius()

### Exercise 4: Data Processor
Function to clean and process sensor data

### Exercise 5: Statistics
Functions for mean, median, standard deviation

## Tomorrow: Day 6 - Lists and Tuples
