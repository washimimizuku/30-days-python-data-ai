"""
Day 18: Pandas Grouping and Aggregation - Solutions
"""

import pandas as pd
import numpy as np

# Exercise 1
sales_data = pd.DataFrame({
    "region": ["North", "South", "North", "East", "South", "West", "East", "North"],
    "product": ["A", "B", "A", "C", "B", "A", "C", "B"],
    "sales": [100, 150, 120, 200, 180, 90, 210, 140],
    "quantity": [10, 15, 12, 20, 18, 9, 21, 14]
})

print("Exercise 1:")
print("Sales data:")
print(sales_data)
print()

# Group by region
region_sales = sales_data.groupby("region")["sales"].sum()
print("Total sales by region:")
print(region_sales)
print()

# Group by product
product_avg = sales_data.groupby("product")["sales"].mean()
print("Average sales by product:")
print(product_avg)
print()

# Exercise 2
print("Exercise 2:")
multi_agg = sales_data.groupby("region").agg({
    "sales": ["sum", "mean", "count"],
    "quantity": ["sum", "mean"]
})
print("Multiple aggregations by region:")
print(multi_agg)
print()

# Exercise 3
print("Exercise 3:")
pivot = sales_data.pivot_table(
    values="sales",
    index="region",
    columns="product",
    aggfunc="sum",
    fill_value=0
)
print("Pivot table (sales by region and product):")
print(pivot)
print()

# Exercise 4
print("Exercise 4:")
sales_data["normalized_sales"] = sales_data.groupby("region")["sales"].transform(
    lambda x: (x - x.mean()) / x.std()
)
print("Sales normalized within each region:")
print(sales_data[["region", "sales", "normalized_sales"]])
print()

# Exercise 5
print("Exercise 5:")
np.random.seed(42)
sensor_data = pd.DataFrame({
    "timestamp": pd.date_range("2024-01-01", periods=24, freq="H"),
    "location": np.random.choice(["Building A", "Building B", "Building C"], 24),
    "sensor_id": np.random.choice([101, 102, 103], 24),
    "temperature": np.random.uniform(20, 30, 24),
    "humidity": np.random.uniform(40, 80, 24)
})

# Add hour for grouping
sensor_data["hour"] = sensor_data["timestamp"].dt.hour

# Group by location
location_stats = sensor_data.groupby("location").agg({
    "temperature": ["mean", "min", "max"],
    "humidity": ["mean", "min", "max"]
}).round(2)

print("Statistics by location:")
print(location_stats)
print()

# Group by hour of day
hourly_avg = sensor_data.groupby("hour")[["temperature", "humidity"]].mean().round(2)
print("Average readings by hour:")
print(hourly_avg.head(10))
print()

# Bonus
print("Bonus - Multi-level grouping:")
multi_group = sensor_data.groupby(["location", "sensor_id"]).agg({
    "temperature": ["count", "mean", "std"],
    "humidity": ["mean", "std"]
}).round(2)
print(multi_group)
print()

# Find peak temperature time per location
peak_temps = sensor_data.loc[sensor_data.groupby("location")["temperature"].idxmax()]
print("Peak temperature time per location:")
print(peak_temps[["location", "timestamp", "temperature"]])
