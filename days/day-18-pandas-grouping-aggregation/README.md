# Day 18: Pandas - Grouping and Aggregation

## 📖 Learning Objectives
- Use groupby() for data aggregation
- Apply multiple aggregation functions
- Create pivot tables
- Transform data within groups
- Analyze data by categories

## Theory

### GroupBy Basics
```python
# Group by single column
grouped = df.groupby('sensor_id')
grouped.mean()  # Average per sensor

# Group by multiple columns
df.groupby(['location', 'sensor_id']).mean()
```

### Aggregation Functions
```python
# Single aggregation
df.groupby('sensor_id')['temperature'].mean()

# Multiple aggregations
df.groupby('sensor_id').agg({
    'temperature': ['mean', 'min', 'max'],
    'humidity': ['mean', 'std']
})

# Custom aggregations
df.groupby('sensor_id').agg({
    'temperature': lambda x: x.max() - x.min()
})
```

### Pivot Tables
```python
# Create pivot table
pivot = pd.pivot_table(
    df,
    values='temperature',
    index='date',
    columns='sensor_id',
    aggfunc='mean'
)
```

### Transform
```python
# Normalize within groups
df['normalized'] = df.groupby('sensor_id')['temperature'].transform(
    lambda x: (x - x.mean()) / x.std()
)
```

## 💻 Exercises
Complete `exercise.py`

## Tomorrow: Day 19 - Working with CSV and JSON
