"""
Day 6: Lists and Tuples - Solutions
"""

# Exercise 1: Sensor Reading Buffer
sensor_readings = []

# Add first 5 readings
readings_batch_1 = [23.5, 24.1, 23.8, 25.0, 24.5]
for reading in readings_batch_1:
    sensor_readings.append(reading)

# Add next 5 readings
readings_batch_2 = [26.2, 25.8, 24.9, 25.5, 26.0]
for reading in readings_batch_2:
    sensor_readings.append(reading)

# Add one more (11th reading)
sensor_readings.append(27.1)

# Keep only last 10 (remove oldest)
sensor_readings = sensor_readings[-10:]
# Alternative: sensor_readings.pop(0)

print("Exercise 1:")
print(f"Sensor buffer (last 10): {sensor_readings}")
print()

# Exercise 2: Data Filtering
temperatures = [23.5, -5.2, 45.0, 60.5, 18.3, -2.0, 35.7, 55.0, 22.1]

valid_temps = []
for temp in temperatures:
    if 0 <= temp <= 50:
        valid_temps.append(temp)

print("Exercise 2:")
print(f"Original: {temperatures}")
print(f"Valid (0-50): {valid_temps}")
print()

# Exercise 3: Coordinate System
point_a = (10, 20)
point_b = (30, 40)

x1, y1 = point_a
x2, y2 = point_b

distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

coordinates = [(0, 0), (10, 10), (20, 5), (15, 25)]

x_coords = [coord[0] for coord in coordinates]
y_coords = [coord[1] for coord in coordinates]

print("Exercise 3:")
print(f"Point A: {point_a}, Point B: {point_b}")
print(f"Distance: {distance:.2f}")
print(f"All coordinates: {coordinates}")
print(f"X coordinates: {x_coords}")
print(f"Y coordinates: {y_coords}")
print()

# Exercise 4: Data Pipeline
raw_data = [100, 105, 98, 200, 102, 99, 180, 101, 103, 97]

# Step 1: Remove outliers
cleaned_data = [x for x in raw_data if x <= 150]

# Step 2: Normalize
min_val = min(cleaned_data)
max_val = max(cleaned_data)
normalized_data = [(x - min_val) / (max_val - min_val) for x in cleaned_data]

# Step 3: Round
final_data = [round(x, 2) for x in normalized_data]

print("Exercise 4:")
print(f"Raw data: {raw_data}")
print(f"Cleaned (outliers removed): {cleaned_data}")
print(f"Normalized: {normalized_data}")
print(f"Final (rounded): {final_data}")
print()

# Exercise 5: Time Series Data
timestamps = ["2024-01-01 00:00", "2024-01-01 01:00", "2024-01-01 02:00", 
              "2024-01-01 03:00", "2024-01-01 04:00"]
values = [23.5, 24.1, 23.8, 25.0, 24.5]

max_value = max(values)
max_index = values.index(max_value)
max_timestamp = timestamps[max_index]

average = sum(values) / len(values)

above_avg = [v for v in values if v > average]

print("Exercise 5:")
print(f"Time series: {len(values)} readings")
print(f"Maximum: {max_value} at {max_timestamp}")
print(f"Average: {average:.2f}")
print(f"Above average: {above_avg}")
print()

# Bonus Challenge
time_series = list(zip(timestamps, values))
sorted_series = sorted(time_series, key=lambda x: x[1], reverse=True)
top_3 = sorted_series[:3]

print("Bonus Challenge:")
print(f"Time series (timestamp, value): {time_series}")
print(f"Top 3 readings:")
for ts, val in top_3:
    print(f"  {ts}: {val}")
