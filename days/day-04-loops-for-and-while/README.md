# Day 4: Loops - for and while

## 📖 Learning Objectives (15 min)

- Use for loops to iterate over sequences
- Use while loops for conditional iteration
- Understand break and continue
- Work with range() function

---

## Theory

### For Loops

```python
# Iterate over list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Iterate over string
for char in "Python":
    print(char)

# Iterate over range
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)
```

### Range Function

```python
range(5)           # 0, 1, 2, 3, 4
range(1, 6)        # 1, 2, 3, 4, 5
range(0, 10, 2)    # 0, 2, 4, 6, 8 (step=2)
range(10, 0, -1)   # 10, 9, 8, ..., 1 (countdown)
```

### While Loops

```python
count = 0
while count < 5:
    print(count)
    count += 1

# Infinite loop (use with caution!)
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == "quit":
        break
```

### Break and Continue

```python
# Break - exit loop
for i in range(10):
    if i == 5:
        break  # Stop loop
    print(i)  # Prints 0-4

# Continue - skip to next iteration
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)  # Prints 1, 3, 5, 7, 9
```

### Enumerate

```python
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# 0: apple
# 1: banana
# 2: cherry
```

---

## 💻 Exercises (40 min)

Complete `exercise.py`

### Exercise 1: Sum Calculator
Calculate sum of numbers 1 to 100

### Exercise 2: Data Processing
Process list of temperatures, find average

### Exercise 3: Pattern Finder
Find all even numbers in a list

### Exercise 4: Validation Loop
Keep asking for input until valid

### Exercise 5: Data Aggregation
Calculate statistics from sensor readings

---

## Tomorrow: Day 5 - Functions
