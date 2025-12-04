"""
Day 9: Error Handling - Solutions
"""

# Exercise 1
print("Exercise 1:")
try:
    number = int("abc")
except ValueError as e:
    print(f"Cannot convert: {e}")
print()

# Exercise 2
print("Exercise 2:")
try:
    with open("nonexistent.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found!")
print()

# Exercise 3
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

print("Exercise 3:")
print(f"10 / 2 = {safe_divide(10, 2)}")
print(f"10 / 0 = {safe_divide(10, 0)}")
print()

# Exercise 4
def validate_age(age_str):
    try:
        age = int(age_str)
        if 0 <= age <= 120:
            return age
        else:
            raise ValueError("Age must be between 0 and 120")
    except ValueError as e:
        print(f"Invalid age: {e}")
        return None

print("Exercise 4:")
print(f"Valid: {validate_age('25')}")
print(f"Invalid: {validate_age('150')}")
print(f"Invalid: {validate_age('abc')}")
print()

# Exercise 5
data_points = ["23.5", "invalid", "45.2", None, "67.8"]
valid_data = []

print("Exercise 5:")
for item in data_points:
    try:
        value = float(item)
        valid_data.append(value)
    except (ValueError, TypeError) as e:
        print(f"Skipping invalid data: {item}")

print(f"Valid data: {valid_data}")
print()

# Bonus
class DataValidationError(Exception):
    pass

def validate_temperature(temp):
    if temp < -50 or temp > 50:
        raise DataValidationError(f"Temperature {temp} out of range")
    return temp

print("Bonus:")
try:
    validate_temperature(25)
    print("25°C is valid")
    validate_temperature(100)
except DataValidationError as e:
    print(f"Validation error: {e}")
