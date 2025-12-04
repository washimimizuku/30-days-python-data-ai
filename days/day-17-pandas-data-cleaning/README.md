# Day 17: Pandas - Data Cleaning

## 📖 Learning Objectives (15 min)

- Handle missing data (NaN values)
- Remove duplicates
- Convert data types
- Detect and handle outliers
- Clean string data
- Validate data quality

---

## Theory

### Missing Data

```python
import pandas as pd
import numpy as np

# Detect missing values
df.isnull()          # Boolean DataFrame
df.isnull().sum()    # Count per column
df.notnull()         # Opposite of isnull()

# Drop missing values
df.dropna()          # Drop rows with any NaN
df.dropna(subset=['temperature'])  # Drop if specific column is NaN
df.dropna(thresh=2)  # Keep rows with at least 2 non-NaN values

# Fill missing values
df.fillna(0)         # Fill with 0
df.fillna(df.mean()) # Fill with mean
df.fillna(method='ffill')  # Forward fill
df.fillna(method='bfill')  # Backward fill
```

### Duplicates

```python
# Detect duplicates
df.duplicated()      # Boolean Series
df.duplicated().sum()  # Count

# Remove duplicates
df.drop_duplicates()
df.drop_duplicates(subset=['sensor_id'])  # Based on specific columns
df.drop_duplicates(keep='last')  # Keep last occurrence
```

### Data Type Conversion

```python
# Check types
df.dtypes

# Convert types
df['sensor_id'] = df['sensor_id'].astype(int)
df['temperature'] = pd.to_numeric(df['temperature'], errors='coerce')
df['date'] = pd.to_datetime(df['date'])

# Handle errors
pd.to_numeric(df['value'], errors='coerce')  # Invalid → NaN
pd.to_numeric(df['value'], errors='ignore')  # Keep original if fails
```

### Outlier Detection

```python
# IQR Method
Q1 = df['temperature'].quantile(0.25)
Q3 = df['temperature'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter outliers
df_clean = df[
    (df['temperature'] >= lower_bound) &
    (df['temperature'] <= upper_bound)
]

# Z-score method
from scipy import stats
z_scores = np.abs(stats.zscore(df['temperature']))
df_clean = df[z_scores < 3]
```

### String Cleaning

```python
# Remove whitespace
df['name'] = df['name'].str.strip()

# Case conversion
df['name'] = df['name'].str.lower()
df['name'] = df['name'].str.upper()

# Replace
df['text'] = df['text'].str.replace('old', 'new')

# Extract patterns
df['code'] = df['text'].str.extract(r'([A-Z]{3})')
```

### Data Validation

```python
# Check ranges
valid_temp = df['temperature'].between(-50, 50)
df_valid = df[valid_temp]

# Check for specific values
valid_status = df['status'].isin(['active', 'inactive'])

# Custom validation
def validate_sensor_id(sid):
    return 100 <= sid <= 999

df['valid'] = df['sensor_id'].apply(validate_sensor_id)
```

---

## 💻 Exercises (40 min)

Complete `exercise.py`

---

## Tomorrow: Day 18 - Pandas Grouping and Aggregation
