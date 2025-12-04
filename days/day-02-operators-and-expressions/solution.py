"""
Day 2: Operators and Expressions - Solutions
"""

# Exercise 1: Age Checker
age = 25

can_vote = age >= 18
can_drink = age >= 21
can_retire = age >= 65

print("Exercise 1:")
print(f"Age: {age}")
print(f"Can vote: {can_vote}")
print(f"Can drink: {can_drink}")
print(f"Can retire: {can_retire}")
print()

# Exercise 2: Temperature Classifier
temperature = 22

is_freezing = temperature < 0
is_cold = 0 <= temperature <= 15
is_moderate = 16 <= temperature <= 25
is_hot = temperature > 25

print("Exercise 2:")
print(f"Temperature: {temperature}°C")
print(f"Freezing: {is_freezing}")
print(f"Cold: {is_cold}")
print(f"Moderate: {is_moderate}")
print(f"Hot: {is_hot}")
print()

# Exercise 3: Data Validation
username = "alice_data"
user_age = 25
email = "alice@example.com"

valid_username = 3 <= len(username) <= 20
valid_age = 0 <= user_age <= 120
valid_email = "@" in email
all_valid = valid_username and valid_age and valid_email

print("Exercise 3:")
print(f"Username '{username}' valid: {valid_username}")
print(f"Age {user_age} valid: {valid_age}")
print(f"Email '{email}' valid: {valid_email}")
print(f"All valid: {all_valid}")
print()

# Exercise 4: Logical Combinations
number = 15

even_and_positive = number % 2 == 0 and number > 0
div_by_3_or_5 = number % 3 == 0 or number % 5 == 0
not_in_range = not (10 <= number <= 20)

print("Exercise 4:")
print(f"Number: {number}")
print(f"Even AND positive: {even_and_positive}")
print(f"Divisible by 3 OR 5: {div_by_3_or_5}")
print(f"NOT in range 10-20: {not_in_range}")
print()

# Exercise 5: Data Quality Check
temperature = 25.5
humidity = 65.0
pressure = 1013.25

valid_temp = -50 <= temperature <= 50
valid_humidity = 0 <= humidity <= 100
valid_pressure = 900 <= pressure <= 1100
all_present = temperature is not None and humidity is not None and pressure is not None
data_valid = valid_temp and valid_humidity and valid_pressure and all_present

print("Exercise 5:")
print(f"Temperature: {temperature}°C - Valid: {valid_temp}")
print(f"Humidity: {humidity}% - Valid: {valid_humidity}")
print(f"Pressure: {pressure} hPa - Valid: {valid_pressure}")
print(f"All present: {all_present}")
print(f"Data point valid: {data_valid}")
