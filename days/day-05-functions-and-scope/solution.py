"""
Day 5: Functions - Solutions
"""

# Exercise 1: Calculator Functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

print("Calculator:")
print(f"10 + 5 = {add(10, 5)}")
print(f"10 - 5 = {subtract(10, 5)}")
print(f"10 * 5 = {multiply(10, 5)}")
print(f"10 / 5 = {divide(10, 5)}")
print()

# Exercise 2: Data Validator
def validate_range(value, min_val, max_val):
    return min_val <= value <= max_val

print("Validation:")
print(f"Temperature 25°C valid (-50 to 50): {validate_range(25, -50, 50)}")
print(f"Humidity 150% valid (0 to 100): {validate_range(150, 0, 100)}")
print()

# Exercise 3: Temperature Converter
def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print("Temperature Conversion:")
print(f"25°C = {celsius_to_fahrenheit(25):.1f}°F")
print(f"77°F = {fahrenheit_to_celsius(77):.1f}°C")
print()

# Exercise 4: Data Processor
def clean_sensor_data(readings, max_valid=50):
    """Remove readings above max_valid"""
    return [r for r in readings if r <= max_valid]

sensor_data = [25.5, 26.0, 100.0, 25.8, 26.1]
cleaned = clean_sensor_data(sensor_data)
print(f"Original: {sensor_data}")
print(f"Cleaned: {cleaned}")
print()

# Exercise 5: Statistics Functions
def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

def calculate_median(numbers):
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_nums[mid-1] + sorted_nums[mid]) / 2
    return sorted_nums[mid]

def calculate_std_dev(numbers):
    mean = calculate_mean(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return variance ** 0.5

data = [10, 12, 23, 23, 16, 23, 21, 16]
print("Statistics:")
print(f"Mean: {calculate_mean(data):.2f}")
print(f"Median: {calculate_median(data):.2f}")
print(f"Std Dev: {calculate_std_dev(data):.2f}")
