# Day 21: DateTime Handling

## 📖 Learning Objectives
- Work with datetime objects
- Parse and format dates
- Perform date arithmetic
- Handle timezones
- Work with time series data

## Theory

### Creating Datetimes
```python
from datetime import datetime, timedelta, date

# Current time
now = datetime.now()
today = date.today()

# Specific datetime
dt = datetime(2024, 1, 15, 14, 30, 0)
```

### Date Arithmetic
```python
# Add/subtract time
tomorrow = now + timedelta(days=1)
last_week = now - timedelta(weeks=1)
two_hours_later = now + timedelta(hours=2)

# Difference between dates
diff = date2 - date1
days_diff = diff.days
```

### Formatting and Parsing
```python
# Format datetime as string
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
formatted = now.strftime("%B %d, %Y")  # January 15, 2024

# Parse string to datetime
dt = datetime.strptime("2024-01-15", "%Y-%m-%d")
```

### Pandas DateTime
```python
# Create date range
dates = pd.date_range('2024-01-01', periods=30, freq='D')

# Parse dates in DataFrame
df['date'] = pd.to_datetime(df['date'])

# Extract components
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day_name'] = df['date'].dt.day_name()
```

## 💻 Exercises
Complete `exercise.py`

## Tomorrow: Day 22 - Regular Expressions
