# Day 16: Pandas - DataFrames and Series

## 📖 Learning Objectives (15 min)

- Understand DataFrames and Series
- Create DataFrames from various sources
- Select, filter, and manipulate data
- Use loc and iloc for indexing
- Perform basic data operations

---

## Theory

### What is Pandas?

Pandas is the primary library for data manipulation in Python:
- Built on NumPy
- DataFrames for tabular data
- Series for 1D data
- Powerful data analysis tools

### Series (1D Data)

```python
import pandas as pd

# Create Series
temperatures = pd.Series([23.5, 24.1, 23.8, 25.0])
print(temperatures)

# With custom index
temps = pd.Series([23.5, 24.1, 23.8], index=['Mon', 'Tue', 'Wed'])
print(temps['Mon'])  # 23.5
```

### DataFrames (2D Data)

```python
# From dictionary
data = {
    'sensor_id': [101, 102, 103],
    'temperature': [23.5, 24.1, 22.8],
    'humidity': [65, 62, 68]
}
df = pd.DataFrame(data)

# From list of dictionaries
data = [
    {'sensor_id': 101, 'temp': 23.5},
    {'sensor_id': 102, 'temp': 24.1}
]
df = pd.DataFrame(data)

# From CSV
df = pd.read_csv('data.csv')
```

### Viewing Data

```python
df.head()        # First 5 rows
df.tail(3)       # Last 3 rows
df.info()        # Data types and info
df.describe()    # Statistical summary
df.shape         # (rows, columns)
df.columns       # Column names
```

### Selecting Data

```python
# Select column (returns Series)
temps = df['temperature']

# Select multiple columns (returns DataFrame)
subset = df[['sensor_id', 'temperature']]

# Select rows by condition
hot = df[df['temperature'] > 24]

# Multiple conditions
filtered = df[(df['temperature'] > 23) & (df['humidity'] < 70)]
```

### loc and iloc

```python
# loc: label-based
df.loc[0]                    # First row
df.loc[0, 'temperature']     # Specific cell
df.loc[0:2, ['sensor_id', 'temperature']]  # Slice

# iloc: position-based
df.iloc[0]                   # First row
df.iloc[0, 1]                # First row, second column
df.iloc[0:3, 0:2]            # Slice by position
```

### Adding/Modifying Columns

```python
# Add new column
df['temp_f'] = df['temperature'] * 9/5 + 32

# Modify existing
df['temperature'] = df['temperature'] + 1

# Delete column
df = df.drop('temp_f', axis=1)
# or
del df['temp_f']
```

### Basic Operations

```python
# Statistics
df['temperature'].mean()
df['temperature'].median()
df['temperature'].std()
df['temperature'].min()
df['temperature'].max()

# Sorting
df.sort_values('temperature')
df.sort_values('temperature', ascending=False)

# Unique values
df['sensor_id'].unique()
df['sensor_id'].nunique()  # Count of unique
```

---

## 💻 Exercises (40 min)

Complete `exercise.py`

### Exercise 1: Create DataFrames
Practice creating DataFrames from different sources

### Exercise 2: Data Selection
Select and filter data using various methods

### Exercise 3: Data Manipulation
Add, modify, and delete columns

### Exercise 4: Sensor Data Analysis
Analyze real sensor data

### Exercise 5: Data Aggregation
Calculate statistics and summaries

---

## ✅ Quiz (5 min)

See `quiz.md`

---

## 🎯 Key Takeaways

- DataFrames are 2D tables, Series are 1D arrays
- Use loc for label-based indexing, iloc for position-based
- Boolean indexing for filtering: `df[df['col'] > value]`
- Easy to add/modify columns
- Built-in statistical functions

---

## Tomorrow: Day 17 - Pandas Data Cleaning

We'll learn how to clean and prepare messy data.
