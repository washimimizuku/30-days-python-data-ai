"""
Day 19: Working with CSV and JSON - Solutions
"""

import pandas as pd
import json
import csv
import os

# Exercise 1
print("Exercise 1:")
data = {
    "id": [1, 2, 3, 4, 5],
    "name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "score": [85, 92, 78, 95, 88]
}
df = pd.DataFrame(data)

# Write to CSV
df.to_csv("students.csv", index=False)
print("Written to students.csv")

# Read CSV
df_read = pd.read_csv("students.csv")
print("Read from CSV:")
print(df_read)
print()

# Exercise 2
print("Exercise 2:")
# Create CSV with edge cases
edge_case_data = """id,name,comment,score
1,"Alice","Great work!",85
2,"Bob","Needs improvement, but good effort",92
3,"Charlie",,78
4,"David","Perfect score!",95"""

with open("students_edge.csv", "w") as f:
    f.write(edge_case_data)

# Read with proper handling
df_edge = pd.read_csv("students_edge.csv", na_values=["", "NA", "null"])
print("CSV with edge cases:")
print(df_edge)
print(f"\nMissing values:\n{df_edge.isnull().sum()}")
print()

# Exercise 3
print("Exercise 3:")
# Write JSON
json_data = {
    "students": [
        {"id": 1, "name": "Alice", "scores": {"math": 85, "science": 90}},
        {"id": 2, "name": "Bob", "scores": {"math": 92, "science": 88}}
    ],
    "class": "Data Science 101",
    "year": 2024
}

with open("students.json", "w") as f:
    json.dump(json_data, f, indent=2)
print("Written to students.json")

# Read JSON
with open("students.json", "r") as f:
    loaded_data = json.load(f)
print("Read from JSON:")
print(json.dumps(loaded_data, indent=2))
print()

# Exercise 4
print("Exercise 4:")
# CSV to JSON
df_csv = pd.read_csv("students.csv")
json_from_csv = df_csv.to_dict(orient="records")

with open("students_from_csv.json", "w") as f:
    json.dump(json_from_csv, f, indent=2)
print("Converted CSV to JSON")

# JSON to CSV (flatten nested structure)
students_flat = []
for student in json_data["students"]:
    flat_student = {
        "id": student["id"],
        "name": student["name"],
        "math_score": student["scores"]["math"],
        "science_score": student["scores"]["science"]
    }
    students_flat.append(flat_student)

df_from_json = pd.DataFrame(students_flat)
df_from_json.to_csv("students_from_json.csv", index=False)
print("Converted JSON to CSV")
print(df_from_json)
print()

# Exercise 5
print("Exercise 5:")
# Create sensor CSV data
sensor_csv = """timestamp,sensor_id,temperature,humidity
2024-01-01 10:00:00,101,23.5,65.2
2024-01-01 10:05:00,102,24.1,62.8
2024-01-01 10:10:00,103,22.8,68.5
2024-01-01 10:15:00,101,23.9,64.8"""

with open("sensors.csv", "w") as f:
    f.write(sensor_csv)

# Read and process
df_sensors = pd.read_csv("sensors.csv", parse_dates=["timestamp"])

# Enrich data
df_sensors["temp_f"] = df_sensors["temperature"] * 9/5 + 32
df_sensors["status"] = df_sensors.apply(
    lambda row: "normal" if 20 <= row["temperature"] <= 30 else "alert",
    axis=1
)

# Export to JSON
result = {
    "metadata": {
        "total_readings": len(df_sensors),
        "sensors": df_sensors["sensor_id"].unique().tolist(),
        "time_range": {
            "start": df_sensors["timestamp"].min().isoformat(),
            "end": df_sensors["timestamp"].max().isoformat()
        }
    },
    "readings": df_sensors.to_dict(orient="records")
}

# Convert timestamps to strings for JSON serialization
for reading in result["readings"]:
    reading["timestamp"] = reading["timestamp"].isoformat()

with open("sensor_report.json", "w") as f:
    json.dump(result, f, indent=2)

print("Processed sensor data and exported to JSON")
print(f"Total readings: {result['metadata']['total_readings']}")
print(f"Sensors: {result['metadata']['sensors']}")
print()

# Bonus
print("Bonus - Efficient large file handling:")
print("For large files, use chunking:")
print("  df_chunks = pd.read_csv('large.csv', chunksize=1000)")
print("  for chunk in df_chunks:")
print("      process(chunk)")

# Cleanup
for f in ["students.csv", "students_edge.csv", "students.json", 
          "students_from_csv.json", "students_from_json.csv", 
          "sensors.csv", "sensor_report.json"]:
    if os.path.exists(f):
        os.remove(f)
