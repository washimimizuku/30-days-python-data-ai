# Day 1: Setup, Variables, and Data Types

## 📖 Learning Objectives (15 min)

By the end of today, you will:
- Understand Python variables and assignment
- Know the basic data types (int, float, str, bool)
- Perform basic operations with different types
- Use the `print()` and `type()` functions

---

## Theory

### Variables

Variables are containers for storing data. In Python, you don't need to declare the type.

```python
# Variable assignment
name = "Alice"
age = 25
height = 1.75
is_student = True
```

### Data Types

#### 1. Integers (int)
Whole numbers, positive or negative.

```python
count = 100
temperature = -5
year = 2024
```

#### 2. Floats (float)
Decimal numbers.

```python
price = 19.99
pi = 3.14159
temperature = 36.6
```

#### 3. Strings (str)
Text data, enclosed in quotes.

```python
name = "John"
message = 'Hello, World!'
multiline = """This is
a multiline
string"""
```

#### 4. Booleans (bool)
True or False values.

```python
is_active = True
has_permission = False
```

### Type Checking

Use `type()` to check a variable's type:

```python
x = 42
print(type(x))  # <class 'int'>

y = 3.14
print(type(y))  # <class 'float'>
```

### Type Conversion

Convert between types:

```python
# String to int
age = int("25")

# Int to string
age_str = str(25)

# String to float
price = float("19.99")

# Int to float
value = float(10)
```

### Basic Operations

```python
# Arithmetic
x = 10 + 5   # Addition: 15
x = 10 - 5   # Subtraction: 5
x = 10 * 5   # Multiplication: 50
x = 10 / 5   # Division: 2.0
x = 10 // 3  # Floor division: 3
x = 10 % 3   # Modulo: 1
x = 2 ** 3   # Exponentiation: 8

# String operations
greeting = "Hello" + " " + "World"  # Concatenation
repeated = "Ha" * 3  # Repetition: "HaHaHa"
```

### Print Function

```python
# Basic printing
print("Hello, World!")

# Multiple values
print("Name:", name, "Age:", age)

# Formatted strings (f-strings)
print(f"My name is {name} and I'm {age} years old")
```

---

## 💻 Exercises (40 min)

Open `exercise.py` and complete the tasks.

### Exercise 1: Variables and Types
Create variables for:
- Your name (string)
- Your age (integer)
- Your height in meters (float)
- Whether you like Python (boolean)

Print each variable and its type.

### Exercise 2: Type Conversion
Given the string "42", convert it to:
- An integer
- A float

Print the results and their types.

### Exercise 3: Calculations
Calculate:
- The area of a rectangle (length=10, width=5)
- The circumference of a circle (radius=7, use pi=3.14159)
- Your age in days (approximate: age * 365)

### Exercise 4: String Operations
Create a greeting message using:
- String concatenation
- F-strings
- The `*` operator to repeat a character

### Exercise 5: Data for AI
Create variables representing a data point:
```python
user_id = 12345
username = "alice_data"
account_balance = 1250.75
is_premium = True
signup_year = 2023
```

Calculate:
- Years since signup (current_year - signup_year)
- Monthly balance (account_balance / 12)

Print a summary using f-strings.

---

## ✅ Quiz (5 min)

Answer these questions in `quiz.md`:

1. What is the difference between `int` and `float`?
2. How do you check the type of a variable?
3. What does `//` operator do?
4. Can you add an integer and a string directly? Why or why not?
5. What's the output of `print(type(3.0))`?

---

## 🎯 Key Takeaways

- Variables store data and don't need type declaration
- Python has 4 basic types: int, float, str, bool
- Use `type()` to check types
- Use `int()`, `float()`, `str()` to convert types
- F-strings are the modern way to format strings

---

## 📚 Additional Resources

- [Python Official Tutorial - Variables](https://docs.python.org/3/tutorial/introduction.html)
- [Real Python - Variables](https://realpython.com/python-variables/)
- [W3Schools - Python Data Types](https://www.w3schools.com/python/python_datatypes.asp)

---

## Tomorrow: Day 2 - Operators and Expressions

We'll dive deeper into operators and learn about comparison and logical operations.
