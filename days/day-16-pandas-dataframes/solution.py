"""
Day 16: Pandas DataFrames - Solutions
"""

import pandas as pd
import numpy as np

# Exercise 1
data = {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [25, 30, 35, 28],
    "city": ["NYC", "LA", "Chicago", "Houston"]
}
df = pd.DataFrame(data)

print("Exercise 1:")
print("DataFrame from dict:")
print(df)
print()

# From list of dicts
data_list = [
    {"sensor_id": 101, "temp": 23.5, "humidity": 65},
    {"sensor_id": 102, "temp": 24.1, "humidity": 62},
    {"sensor_id": 103, "temp": 22.8, "humidity": 68}
]
df_sensors = pd.DataFrame(data_list)
print("DataFrame from list of dicts:")
print(df_sensors)
print()

# From NumPy array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
df_numpy = pd.DataFrame(arr, columns=["A", "B", "C"])
print("DataFrame from NumPy:")
print(df_numpy)
print()

# Exercise 2
print("Exercise 2:")
print("First 2 rows:")
print(df.head(2))
print("\nDataFrame info:")
print(df.info())
print("\nStatistics:")
print(df.describe())
print()

# Select columns
print("Names only:")
print(df["name"])
print("\nMultiple columns:")
print(df[["name", "age"]])
print()

# Filter rows
print("People over 28:")
print(df[df["age"] > 28])
print()

# Exercise 3
df_copy = df.copy()
df_copy["country"] = "USA"
df_copy["age_group"] = df_copy["age"].apply(lambda x: "young" if x < 30 else "adult")

print("Exercise 3:")
print("With new columns:")
print(df_copy)
print()

# Modify column
df_copy["age"] = df_copy["age"] + 1
print("After incrementing age:")
print(df_copy[["name", "age"]])
print()

# Delete column
df_copy = df_copy.drop("country", axis=1)
print("After dropping country:")
print(df_copy.columns.tolist())
print()

# Exercise 4
print("Exercise 4:")
print("Using loc (label-based):")
print(df.loc[0, "name"])
print("\nUsing iloc (position-based):")
print(df.iloc[0, 0])
print("\nSlicing with loc:")
print(df.loc[0:2, ["name", "age"]])
print()

# Boolean indexing
print("NYC residents:")
print(df[df["city"] == "NYC"])
print("\nAge between 25 and 30:")
print(df[(df["age"] >= 25) & (df["age"] <= 30)])
print()

# Exercise 5
np.random.seed(42)
sensor_data = pd.DataFrame({
    "timestamp": pd.date_range("2024-01-01", periods=20, freq="H"),
    "sensor_id": np.random.choice([101, 102, 103], 20),
    "temperature": np.random.uniform(20, 30, 20),
    "humidity": np.random.uniform(40, 80, 20)
})

print("Exercise 5:")
print("Sensor data:")
print(sensor_data.head())
print()

# Statistics per sensor
print("Statistics by sensor:")
print(sensor_data.groupby("sensor_id").agg({
    "temperature": ["mean", "min", "max"],
    "humidity": ["mean", "min", "max"]
}))
print()

# Find anomalies (temp > 28 or humidity > 75)
anomalies = sensor_data[
    (sensor_data["temperature"] > 28) | (sensor_data["humidity"] > 75)
]
print(f"Anomalies found: {len(anomalies)}")
print(anomalies[["timestamp", "sensor_id", "temperature", "humidity"]])
print()

# Bonus
print("Bonus - Method chaining:")
result = (sensor_data
    .query("temperature > 25")
    .assign(temp_f=lambda x: x["temperature"] * 9/5 + 32)
    .groupby("sensor_id")
    .agg({"temp_f": ["mean", "count"]})
    .round(2)
)
print(result)
