"""
Day 3: Control Flow - Solutions
"""

# Exercise 1: Grade Calculator
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score} -> Grade: {grade}")

# Exercise 2: Temperature Advisor
temperature = 15

if temperature < 0:
    advice = "Wear heavy coat"
elif temperature <= 15:
    advice = "Wear jacket"
elif temperature <= 25:
    advice = "Wear light clothes"
else:
    advice = "Wear shorts"

print(f"Temperature: {temperature}°C -> {advice}")

# Exercise 3: Data Validator
value = 42
data_type = "temperature"

if data_type == "temperature":
    is_valid = -50 <= value <= 50
elif data_type == "humidity":
    is_valid = 0 <= value <= 100
elif data_type == "pressure":
    is_valid = 900 <= value <= 1100
else:
    is_valid = False

print(f"{data_type}: {value} -> Valid: {is_valid}")

# Exercise 4: Anomaly Detector
sensor_value = 105
normal_min = 20
normal_max = 80

is_anomaly = sensor_value < normal_min or sensor_value > normal_max

if sensor_value > 2 * normal_max or sensor_value < 0.5 * normal_min:
    severity = "Critical"
elif is_anomaly:
    severity = "Warning"
else:
    severity = "Normal"

print(f"Value: {sensor_value}, Range: [{normal_min}, {normal_max}]")
print(f"Anomaly: {is_anomaly}, Severity: {severity}")

# Exercise 5: User Access Control
user_role = "admin"
is_active = True
account_age_days = 30

if user_role == "admin" and is_active:
    access_level = "full_access"
elif user_role == "user" and is_active:
    if account_age_days > 7:
        access_level = "read_write"
    else:
        access_level = "read_only"
elif user_role == "guest" or not is_active:
    access_level = "no_access"
else:
    access_level = "no_access"

print(f"Role: {user_role}, Active: {is_active}, Age: {account_age_days} days")
print(f"Access Level: {access_level}")
