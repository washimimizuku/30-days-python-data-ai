"""
Day 6: Lists and Tuples - Exercises
Complete each exercise below
"""

# Exercise 1: Sensor Reading Buffer
# TODO: Create a list to store the last 10 sensor readings
sensor_readings = []

# TODO: Add these readings one by one: 23.5, 24.1, 23.8, 25.0, 24.5
# Use append()


# TODO: Add 26.2, 25.8, 24.9, 25.5, 26.0


# TODO: Add one more reading 27.1 (should have 11 readings now)


# TODO: Keep only the last 10 readings (remove the oldest)


# TODO: Print the current buffer


# Exercise 2: Data Filtering
# TODO: Given this list of temperatures, filter out readings below 0 and above 50
temperatures = [23.5, -5.2, 45.0, 60.5, 18.3, -2.0, 35.7, 55.0, 22.1]

# TODO: Create a new list with only valid readings (0 to 50)
valid_temps = []


# TODO: Print valid temperatures


# Exercise 3: Coordinate System
# TODO: Create tuples for these coordinates
point_a = (10, 20)
point_b = (30, 40)

# TODO: Unpack the coordinates
# x1, y1 = ?
# x2, y2 = ?

# TODO: Calculate distance between points
# distance = sqrt((x2-x1)^2 + (y2-y1)^2)
# Hint: Use ** 0.5 for square root


# TODO: Create a list of coordinate tuples
coordinates = [(0, 0), (10, 10), (20, 5), (15, 25)]

# TODO: Extract all x coordinates
# x_coords = ?

# TODO: Extract all y coordinates
# y_coords = ?


# Exercise 4: Data Pipeline
# TODO: Start with this raw data
raw_data = [100, 105, 98, 200, 102, 99, 180, 101, 103, 97]

# TODO: Step 1 - Remove outliers (values > 150)
# cleaned_data = ?

# TODO: Step 2 - Normalize to 0-1 range
# normalized = [(x - min) / (max - min) for x in cleaned_data]
# normalized_data = ?

# TODO: Step 3 - Round to 2 decimal places
# final_data = ?

# TODO: Print each step


# Exercise 5: Time Series Data
# TODO: Create parallel lists for time series
timestamps = ["2024-01-01 00:00", "2024-01-01 01:00", "2024-01-01 02:00", 
              "2024-01-01 03:00", "2024-01-01 04:00"]
values = [23.5, 24.1, 23.8, 25.0, 24.5]

# TODO: Find the maximum value and its timestamp
# max_value = ?
# max_index = ?
# max_timestamp = ?

# TODO: Calculate average value
# average = ?

# TODO: Find values above average
# above_avg = ?

# TODO: Print summary


# Bonus Challenge
# TODO: Create a list of tuples combining timestamps and values
# time_series = ?

# TODO: Sort by value (descending)
# sorted_series = ?

# TODO: Get top 3 readings
# top_3 = ?
