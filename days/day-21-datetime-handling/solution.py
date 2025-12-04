"""
Day 21: DateTime Handling - Solutions
"""

from datetime import datetime, timedelta, date, time
import time as time_module

# Exercise 1
print("Exercise 1: Basic DateTime Operations")
now = datetime.now()
today = date.today()
current_time = datetime.now().time()

print(f"Current datetime: {now}")
print(f"Today's date: {today}")
print(f"Current time: {current_time}")

# Create specific datetime
specific_date = datetime(2024, 1, 15, 14, 30, 0)
print(f"Specific datetime: {specific_date}")

# Extract components
print(f"Year: {now.year}")
print(f"Month: {now.month}")
print(f"Day: {now.day}")
print(f"Hour: {now.hour}")
print(f"Minute: {now.minute}")
print()

# Exercise 2
print("Exercise 2: DateTime Arithmetic")
now = datetime.now()

# Add/subtract time
tomorrow = now + timedelta(days=1)
yesterday = now - timedelta(days=1)
next_week = now + timedelta(weeks=1)
two_hours_later = now + timedelta(hours=2)

print(f"Now: {now}")
print(f"Tomorrow: {tomorrow}")
print(f"Yesterday: {yesterday}")
print(f"Next week: {next_week}")
print(f"Two hours later: {two_hours_later}")

# Calculate difference
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)
difference = end_date - start_date

print(f"\nDays between dates: {difference.days}")
print(f"Total seconds: {difference.total_seconds()}")
print()

# Exercise 3
print("Exercise 3: String Formatting and Parsing")
now = datetime.now()

# Format datetime as string
formatted_1 = now.strftime("%Y-%m-%d")
formatted_2 = now.strftime("%B %d, %Y")
formatted_3 = now.strftime("%Y-%m-%d %H:%M:%S")
formatted_4 = now.strftime("%I:%M %p")

print(f"ISO format: {formatted_1}")
print(f"Long format: {formatted_2}")
print(f"Full datetime: {formatted_3}")
print(f"12-hour time: {formatted_4}")

# Parse string to datetime
date_string_1 = "2024-01-15"
date_string_2 = "January 15, 2024"
date_string_3 = "2024-01-15 14:30:00"

parsed_1 = datetime.strptime(date_string_1, "%Y-%m-%d")
parsed_2 = datetime.strptime(date_string_2, "%B %d, %Y")
parsed_3 = datetime.strptime(date_string_3, "%Y-%m-%d %H:%M:%S")

print(f"\nParsed from '{date_string_1}': {parsed_1}")
print(f"Parsed from '{date_string_2}': {parsed_2}")
print(f"Parsed from '{date_string_3}': {parsed_3}")
print()

# Exercise 4
print("Exercise 4: Working with Timestamps")
now = datetime.now()

# Datetime to timestamp
timestamp = now.timestamp()
print(f"Current datetime: {now}")
print(f"As timestamp: {timestamp}")

# Timestamp to datetime
dt_from_timestamp = datetime.fromtimestamp(timestamp)
print(f"Back to datetime: {dt_from_timestamp}")

# Unix timestamp (seconds since 1970-01-01)
unix_timestamp = int(time_module.time())
print(f"\nUnix timestamp: {unix_timestamp}")
print(f"As datetime: {datetime.fromtimestamp(unix_timestamp)}")
print()

# Exercise 5
print("Exercise 5: Time Series Data")
import pandas as pd

# Create date range
date_range = pd.date_range(start="2024-01-01", end="2024-01-31", freq="D")
print(f"Date range (first 5): {date_range[:5].tolist()}")

# Create time series data
import numpy as np
np.random.seed(42)
time_series = pd.DataFrame({
    "date": pd.date_range("2024-01-01", periods=30, freq="D"),
    "temperature": np.random.uniform(20, 30, 30),
    "humidity": np.random.uniform(40, 80, 30)
})

print(f"\nTime series data (first 5 rows):")
print(time_series.head())

# Filter by date range
start_filter = datetime(2024, 1, 10)
end_filter = datetime(2024, 1, 20)
filtered = time_series[
    (time_series["date"] >= start_filter) & 
    (time_series["date"] <= end_filter)
]
print(f"\nFiltered data (Jan 10-20): {len(filtered)} rows")

# Time-based statistics
time_series["day_of_week"] = time_series["date"].dt.day_name()
weekly_avg = time_series.groupby("day_of_week")["temperature"].mean()
print(f"\nAverage temperature by day of week:")
print(weekly_avg)
print()

# Bonus
print("Bonus: Timezone Handling")
from datetime import timezone

# UTC time
utc_now = datetime.now(timezone.utc)
print(f"UTC time: {utc_now}")
print(f"ISO format: {utc_now.isoformat()}")

# Calculate age
def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year
    if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
        age -= 1
    return age

birth = date(1990, 5, 15)
age = calculate_age(birth)
print(f"\nBirth date: {birth}")
print(f"Age: {age} years")

print("\n" + "="*60)
print("Day 21 Complete! Move to Day 22")
print("="*60)
