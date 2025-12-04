"""
Day 8: File I/O - Solutions
"""

import csv
import os

# Exercise 1: Log File Reader
log_content = """2024-01-01 10:00:00 INFO Application started
2024-01-01 10:05:23 WARNING High memory usage
2024-01-01 10:10:45 ERROR Database connection failed
2024-01-01 10:15:12 INFO Retry successful
2024-01-01 10:20:00 ERROR Timeout occurred"""

with open("log.txt", "w") as f:
    f.write(log_content)

error_count = 0
with open("log.txt", "r") as f:
    for line in f:
        if "ERROR" in line:
            error_count += 1

print("Exercise 1:")
print(f"Error count: {error_count}")
print()

# Exercise 2: CSV Data Writer
sensor_data = [
    {"sensor_id": 101, "temperature": 23.5, "humidity": 65.2},
    {"sensor_id": 102, "temperature": 24.1, "humidity": 62.8},
    {"sensor_id": 103, "temperature": 22.8, "humidity": 68.5}
]

with open("sensors.csv", "w", newline="") as f:
    fieldnames = ["sensor_id", "temperature", "humidity"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for row in sensor_data:
        writer.writerow(row)

print("Exercise 2:")
print(f"Written {len(sensor_data)} rows to sensors.csv")
print()

# Exercise 3: File Statistics
with open("log.txt", "r") as f:
    content = f.read()
    lines = content.split("\n")
    words = content.split()
    chars = len(content)

print("Exercise 3:")
print(f"Lines: {len(lines)}")
print(f"Words: {len(words)}")
print(f"Characters: {chars}")
print()

# Exercise 4: Data Format Converter
with open("sensors.csv", "r") as f:
    reader = csv.DictReader(f)
    print("Exercise 4:")
    for row in reader:
        print(f"Sensor {row['sensor_id']}: {row['temperature']}°C, {row['humidity']}% humidity")
print()

# Exercise 5: Batch File Processor
files_to_create = {
    "data1.txt": "100,200,300",
    "data2.txt": "150,250,350",
    "data3.txt": "120,220,320"
}

for filename, content in files_to_create.items():
    with open(filename, "w") as f:
        f.write(content)

total_sum = 0
for filename in files_to_create.keys():
    with open(filename, "r") as f:
        numbers = [int(x) for x in f.read().split(",")]
        total_sum += sum(numbers)

print("Exercise 5:")
print(f"Total sum from all files: {total_sum}")
print()

# Bonus Challenge
with open("sensors.csv", "r") as f:
    reader = csv.DictReader(f)
    filtered_data = [row for row in reader if float(row["temperature"]) > 23]

with open("sensors_filtered.csv", "w", newline="") as f:
    if filtered_data:
        fieldnames = filtered_data[0].keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in filtered_data:
            writer.writerow(row)

print("Bonus Challenge:")
print(f"Filtered {len(filtered_data)} rows to sensors_filtered.csv")

# Cleanup
for f in ["log.txt", "sensors.csv", "sensors_filtered.csv", "data1.txt", "data2.txt", "data3.txt"]:
    if os.path.exists(f):
        os.remove(f)
