"""
Day 17: Pandas Data Cleaning - Solutions
"""

import pandas as pd
import numpy as np

# Exercise 1
data = {
    "sensor_id": [101, 102, 103, 104, 105],
    "temperature": [23.5, np.nan, 24.8, 25.0, np.nan],
    "humidity": [65, 62, np.nan, 68, 70],
    "status": ["active", "active", None, "active", "error"]
}
df = pd.DataFrame(data)

print("Exercise 1:")
print("Original data:")
print(df)
print("\nMissing values:")
print(df.isnull().sum())
print()

# Fill missing values
df_filled = df.copy()
df_filled["temperature"] = df_filled["temperature"].fillna(df_filled["temperature"].mean())
df_filled["humidity"] = df_filled["humidity"].fillna(method="ffill")
df_filled["status"] = df_filled["status"].fillna("unknown")

print("After filling:")
print(df_filled)
print()

# Drop rows with any missing values
df_dropped = df.dropna()
print(f"After dropping rows with NaN: {len(df_dropped)} rows remaining")
print()

# Exercise 2
data_dup = {
    "id": [1, 2, 2, 3, 4, 4, 5],
    "value": [10, 20, 20, 30, 40, 40, 50]
}
df_dup = pd.DataFrame(data_dup)

print("Exercise 2:")
print("Data with duplicates:")
print(df_dup)
print(f"\nDuplicate rows: {df_dup.duplicated().sum()}")

df_unique = df_dup.drop_duplicates()
print("\nAfter removing duplicates:")
print(df_unique)
print()

# Exercise 3
data_types = {
    "id": ["1", "2", "3", "4"],
    "value": ["10.5", "20.3", "invalid", "40.1"],
    "date": ["2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04"]
}
df_types = pd.DataFrame(data_types)

print("Exercise 3:")
print("Original types:")
print(df_types.dtypes)
print()

# Convert types
df_types["id"] = df_types["id"].astype(int)
df_types["value"] = pd.to_numeric(df_types["value"], errors="coerce")
df_types["date"] = pd.to_datetime(df_types["date"])

print("After conversion:")
print(df_types.dtypes)
print("\nData:")
print(df_types)
print()

# Exercise 4
data_str = {
    "sensor_name": ["  Sensor_A  ", "SENSOR_B", "sensor_c  ", "  Sensor_D"],
    "location": ["Building-A-Floor-1", "Building-B-Floor-2", "Building-A-Floor-3", "Building-C-Floor-1"]
}
df_str = pd.DataFrame(data_str)

print("Exercise 4:")
print("Original strings:")
print(df_str)
print()

# Clean strings
df_str["sensor_name"] = df_str["sensor_name"].str.strip().str.lower().str.replace("_", " ")
df_str["building"] = df_str["location"].str.split("-").str[0]
df_str["floor"] = df_str["location"].str.extract(r"Floor-(\d+)")

print("After cleaning:")
print(df_str)
print()

# Exercise 5
np.random.seed(42)
data_outliers = pd.DataFrame({
    "temperature": np.concatenate([
        np.random.normal(25, 2, 95),
        [50, 60, -10, 55, 65]  # outliers
    ])
})

print("Exercise 5:")
print(f"Data shape: {data_outliers.shape}")
print(f"Temperature range: {data_outliers['temperature'].min():.1f} to {data_outliers['temperature'].max():.1f}")

# IQR method
Q1 = data_outliers["temperature"].quantile(0.25)
Q3 = data_outliers["temperature"].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = data_outliers[
    (data_outliers["temperature"] < lower_bound) | 
    (data_outliers["temperature"] > upper_bound)
]

print(f"\nIQR method:")
print(f"Q1: {Q1:.2f}, Q3: {Q3:.2f}, IQR: {IQR:.2f}")
print(f"Bounds: [{lower_bound:.2f}, {upper_bound:.2f}]")
print(f"Outliers found: {len(outliers)}")

# Remove outliers
df_clean = data_outliers[
    (data_outliers["temperature"] >= lower_bound) & 
    (data_outliers["temperature"] <= upper_bound)
]
print(f"After removing outliers: {len(df_clean)} rows")
print()

# Bonus: Complete pipeline
print("Bonus - Complete cleaning pipeline:")
raw_data = pd.DataFrame({
    "sensor_id": ["S001", "S002", "S002", "S003", "S004", "S005"],
    "temperature": ["23.5", "invalid", "24.8", "25.0", np.nan, "150"],
    "humidity": [65, 62, 62, 68, 70, 55],
    "status": ["  ACTIVE  ", "active", "ACTIVE", None, "ERROR", "active"]
})

cleaned = (raw_data
    .drop_duplicates()
    .assign(
        temperature=lambda x: pd.to_numeric(x["temperature"], errors="coerce"),
        status=lambda x: x["status"].str.strip().str.lower().fillna("unknown")
    )
    .dropna(subset=["temperature"])
    .query("temperature >= 0 and temperature <= 50")
    .reset_index(drop=True)
)

print("\nRaw data:")
print(raw_data)
print("\nCleaned data:")
print(cleaned)
