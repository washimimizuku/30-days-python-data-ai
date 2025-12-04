"""
Day 11: Modules and Imports - Solutions
"""

import math
import datetime
import random

# Exercise 1
print("Exercise 1:")
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Pi: {math.pi}")
print(f"Current datetime: {datetime.datetime.now()}")
print(f"Random number: {random.randint(1, 100)}")
print()

# Exercise 2
from math import sqrt, pow

print("Exercise 2:")
print(f"sqrt(25) = {sqrt(25)}")
print(f"pow(2, 3) = {pow(2, 3)}")
print()

# Exercise 3: Create data_utils.py
data_utils_content = """
def calculate_mean(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def calculate_median(numbers):
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    if n == 0:
        return 0
    mid = n // 2
    if n % 2 == 0:
        return (sorted_nums[mid-1] + sorted_nums[mid]) / 2
    return sorted_nums[mid]

def calculate_std_dev(numbers):
    if not numbers:
        return 0
    mean = calculate_mean(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return variance ** 0.5
"""

with open("data_utils.py", "w") as f:
    f.write(data_utils_content)

import data_utils

print("Exercise 3:")
test_data = [10, 20, 30, 40, 50]
print(f"Data: {test_data}")
print(f"Mean: {data_utils.calculate_mean(test_data)}")
print(f"Median: {data_utils.calculate_median(test_data)}")
print(f"Std Dev: {data_utils.calculate_std_dev(test_data):.2f}")
print()

# Exercise 4
import os
os.makedirs("my_package", exist_ok=True)

with open("my_package/__init__.py", "w") as f:
    f.write("# My data processing package\n")

with open("my_package/validators.py", "w") as f:
    f.write("""
def validate_range(value, min_val, max_val):
    return min_val <= value <= max_val

def validate_type(value, expected_type):
    return isinstance(value, expected_type)
""")

with open("my_package/processors.py", "w") as f:
    f.write("""
def normalize(values):
    min_val, max_val = min(values), max(values)
    return [(v - min_val) / (max_val - min_val) for v in values]

def filter_outliers(values, std_devs=2):
    mean = sum(values) / len(values)
    std = (sum((x - mean) ** 2 for x in values) / len(values)) ** 0.5
    return [v for v in values if abs(v - mean) <= std_devs * std]
""")

print("Exercise 4:")
print("Created package structure:")
print("  my_package/")
print("    __init__.py")
print("    validators.py")
print("    processors.py")
print()

# Exercise 5
print("Exercise 5:")
print(f"Math module contents (first 10): {dir(math)[:10]}")
print(f"\nHelp for math.sqrt:")
print(math.sqrt.__doc__)
print()

# Cleanup
import shutil
os.remove("data_utils.py")
if os.path.exists("__pycache__"):
    shutil.rmtree("__pycache__")
if os.path.exists("my_package"):
    shutil.rmtree("my_package")
