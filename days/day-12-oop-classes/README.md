# Day 12: Object-Oriented Programming - Classes

## 📖 Learning Objectives (15 min)
- Define classes and create objects
- Use __init__ constructor
- Define methods
- Understand self parameter

## Theory

### Basic Class
```python
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Hello, I'm {self.name}"
    
    def is_adult(self):
        return self.age >= 18

# Create instance
user = User("Alice", 25)
print(user.greet())
```

### Class vs Instance Variables
```python
class DataPoint:
    count = 0  # Class variable
    
    def __init__(self, value):
        self.value = value  # Instance variable
        DataPoint.count += 1
```

### Methods
```python
class Calculator:
    def add(self, a, b):
        return a + b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @classmethod
    def from_string(cls, string):
        return cls(int(string))
```

## 💻 Exercises (40 min)

### Exercise 1: Sensor Class
Create class for sensor data

### Exercise 2: User Management
Build user class with methods

### Exercise 3: Data Container
Create class to store and process data

### Exercise 4: Temperature Tracker
Class with history and statistics

### Exercise 5: Bank Account
Class with deposit, withdraw, balance

## Tomorrow: Day 13 - OOP Inheritance
