"""
Day 8: File I/O - Exercises
Complete each exercise below
"""

import csv
import os

# Exercise 1: Log File Reader
# TODO: Create a sample log file
log_content = """2024-01-01 10:00:00 INFO Application started
2024-01-01 10:05:23 WARNING High memory usage
2024-01-01 10:10:45 ERROR Database connection failed
2024-01-01 10:15:12 INFO Retry successful
2024-01-01 10:20:00 ERROR Timeout occurred"""

# TODO: Write to log.txt
# with open("log.txt", "w") as f:
#     f.write(log_content)

# TODO: Read and count ERROR messages
# error_count = 0


# TODO: Print error count


# Exercise 2: CSV Data Writer
# TODO: Create sensor data
sensor_data = [
    {"sensor_id": 101, "temperature": 23.5, "humidity": 65.2},
    {"sensor_id": 102, "temperature": 24.1, "humidity": 62.8},
    {"sensor_id": 103, "temperature": 22.8, "humidity": 68.5}
]

# TODO: Write to sensors.csv
# with open("sensors.csv", "w", newline="") as f:
#     fieldnames = ["sensor_id", "temperature", "humidity"]
#     writer = csv.DictWriter(f, fieldnames=fieldnames)
#     writer.writeheader()
#     for row in sensor_data:
#         writer.writerow(row)


# Exercise 3: File Statistics
# TODO: Read log.txt and calculate:
# - Number of lines
# - Number of words
# - Number of characters


# Exercise 4: Data Format Converter
# TODO: Read sensors.csv and convert to text format
# Format: "Sensor 101: 23.5°C, 65.2% humidity"


# Exercise 5: Batch File Processor
# TODO: Create multiple data files
files_to_create = {
    "data1.txt": "100,200,300",
    "data2.txt": "150,250,350",
    "data3.txt": "120,220,320"
}

# TODO: Write files


# TODO: Read all files and calculate total sum


# Bonus Challenge
# TODO: Read CSV, filter rows where temperature > 23, write to new CSV
