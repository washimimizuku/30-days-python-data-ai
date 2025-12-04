"""
Day 18: Pandas Grouping and Aggregation - Exercises
"""

import pandas as pd
import numpy as np

# Exercise 1: Basic GroupBy
# TODO: Create sales data
sales_data = pd.DataFrame({
    "region": ["North", "South", "North", "East", "South", "West", "East", "North"],
    "product": ["A", "B", "A", "C", "B", "A", "C", "B"],
    "sales": [100, 150, 120, 200, 180, 90, 210, 140],
    "quantity": [10, 15, 12, 20, 18, 9, 21, 14]
})

# TODO: Group by region and calculate total sales


# TODO: Group by product and calculate average sales


# Exercise 2: Multiple Aggregations
# TODO: Calculate multiple statistics per group


# Exercise 3: Pivot Tables
# TODO: Create pivot table showing sales by region and product


# Exercise 4: Transform and Apply
# TODO: Normalize sales within each region


# Exercise 5: Sensor Data Analysis
# TODO: Analyze sensor readings by location and time


# Bonus: Complex multi-level grouping
