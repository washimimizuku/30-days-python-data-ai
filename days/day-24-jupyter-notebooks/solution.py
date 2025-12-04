"""
Day 24: Jupyter Notebooks - Solutions

This file demonstrates what you would do in Jupyter.
For actual practice, use: jupyter notebook
"""

print("="*60)
print("Day 24: Jupyter Notebooks")
print("="*60)
print()

# Exercise 1: Notebook Basics
print("Exercise 1: Notebook Basics")
print("""
In Jupyter Notebook:

1. Create new notebook: New > Python 3
2. Cell types:
   - Code: Python code
   - Markdown: Documentation

3. Keyboard shortcuts:
   - Shift+Enter: Run cell
   - Esc: Command mode
   - Enter: Edit mode
   - A: Insert cell above
   - B: Insert cell below
   - DD: Delete cell

4. Markdown examples:
   # Heading 1
   ## Heading 2
   **bold** *italic*
   - List item
   `code`
""")

# Exercise 2: Data Analysis Example
print("\nExercise 2: Data Analysis in Notebook")
print("\nExample notebook structure:")

# Cell 1: Imports
print("""
# Cell 1 - Imports
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
```
""")

# Cell 2: Load Data
print("""
# Cell 2 - Load Data
```python
df = pd.read_csv('data.csv')
df.head()
```
""")

# Cell 3: Explore
print("""
# Cell 3 - Explore
```python
df.info()
df.describe()
```
""")

# Cell 4: Visualize
print("""
# Cell 4 - Visualize
```python
df['column'].hist()
plt.title('Distribution')
plt.show()
```
""")

# Exercise 3: Markdown Documentation
print("\nExercise 3: Markdown Examples")
print("""
# Data Analysis Report

## Introduction
This analysis explores sensor data from...

## Data Description
- **Source**: Sensor network
- **Period**: January 2024
- **Records**: 1000 readings

## Key Findings
1. Average temperature: 25°C
2. Peak usage: 2PM-4PM
3. Anomalies detected: 5

## Code Example
```python
df.groupby('sensor_id').mean()
```

## Conclusion
The analysis shows...
""")

# Exercise 4: Interactive Exploration
print("\nExercise 4: Interactive Exploration")
import pandas as pd
import numpy as np

# Create sample data
np.random.seed(42)
data = pd.DataFrame({
    'sensor_id': np.random.choice(['A', 'B', 'C'], 100),
    'temperature': np.random.normal(25, 3, 100),
    'humidity': np.random.normal(60, 10, 100)
})

print("Sample data created:")
print(data.head())
print(f"\nShape: {data.shape}")
print(f"\nSummary statistics:")
print(data.describe())

# Exercise 5: Complete Analysis Template
print("\nExercise 5: Complete Analysis Notebook Template")
print("""
# Sensor Data Analysis

## 1. Setup
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
```

## 2. Load Data
```python
df = pd.read_csv('sensor_data.csv')
print(f"Loaded {len(df)} records")
df.head()
```

## 3. Data Cleaning
```python
# Check for missing values
df.isnull().sum()

# Remove outliers
Q1 = df['temperature'].quantile(0.25)
Q3 = df['temperature'].quantile(0.75)
IQR = Q3 - Q1
df_clean = df[
    (df['temperature'] >= Q1 - 1.5*IQR) &
    (df['temperature'] <= Q3 + 1.5*IQR)
]
```

## 4. Exploratory Analysis
```python
# Statistics by sensor
df_clean.groupby('sensor_id').agg({
    'temperature': ['mean', 'std', 'min', 'max']
})
```

## 5. Visualization
```python
# Temperature distribution
plt.figure(figsize=(10, 6))
df_clean['temperature'].hist(bins=30)
plt.title('Temperature Distribution')
plt.xlabel('Temperature (°C)')
plt.ylabel('Frequency')
plt.show()
```

## 6. Conclusions
- Average temperature: 25.3°C
- Sensor A shows highest variance
- No significant anomalies detected
""")

print("\n" + "="*60)
print("Day 24 Complete! Move to Day 25")
print("="*60)
