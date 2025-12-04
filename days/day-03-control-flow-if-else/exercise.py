"""
Day 3: Control Flow - if/else - Exercises
"""

# Exercise 1: Grade Calculator
score = 85  # Change to test

# TODO: Convert score to letter grade
# A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: below 60
# grade = ?

# TODO: Print result


# Exercise 2: Temperature Advisor
temperature = 15  # Change to test

# TODO: Give clothing advice
# < 0: "Wear heavy coat"
# 0-15: "Wear jacket"
# 16-25: "Wear light clothes"
# > 25: "Wear shorts"
# advice = ?

# TODO: Print advice


# Exercise 3: Data Validator
value = 42
data_type = "temperature"  # or "humidity", "pressure"

# TODO: Validate based on type
# temperature: -50 to 50
# humidity: 0 to 100
# pressure: 900 to 1100
# is_valid = ?

# TODO: Print validation result


# Exercise 4: Anomaly Detector
sensor_value = 105
normal_min = 20
normal_max = 80

# TODO: Detect if value is anomaly
# Anomaly if: value < normal_min OR value > normal_max
# is_anomaly = ?

# TODO: Classify severity
# Critical: > 2x normal_max or < 0.5x normal_min
# Warning: outside normal range but not critical
# Normal: within range
# severity = ?

# TODO: Print detection results


# Exercise 5: User Access Control
user_role = "admin"  # or "user", "guest"
is_active = True
account_age_days = 30

# TODO: Determine permissions
# admin + active: full_access
# user + active + age > 7: read_write
# user + active + age <= 7: read_only
# guest or not active: no_access
# access_level = ?

# TODO: Print access level
