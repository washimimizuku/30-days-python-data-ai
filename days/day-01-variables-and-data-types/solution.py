"""
Day 1: Variables and Data Types - Solutions
"""

# Exercise 1: Variables and Types
name = "Alice"
age = 25
height = 1.75
likes_python = True

print("Exercise 1:")
print(f"Name: {name}, Type: {type(name)}")
print(f"Age: {age}, Type: {type(age)}")
print(f"Height: {height}, Type: {type(height)}")
print(f"Likes Python: {likes_python}, Type: {type(likes_python)}")
print()

# Exercise 2: Type Conversion
number_string = "42"
number_int = int(number_string)
number_float = float(number_string)

print("Exercise 2:")
print(f"Integer: {number_int}, Type: {type(number_int)}")
print(f"Float: {number_float}, Type: {type(number_float)}")
print()

# Exercise 3: Calculations
area = 10 * 5
circumference = 2 * 3.14159 * 7
age_in_days = age * 365

print("Exercise 3:")
print(f"Rectangle area: {area}")
print(f"Circle circumference: {circumference:.2f}")
print(f"Age in days: {age_in_days}")
print()

# Exercise 4: String Operations
greeting_concat = "Hello" + " " + "World" + "!"
greeting_fstring = f"Hello {name}!"
line = "-" * 50

print("Exercise 4:")
print(greeting_concat)
print(greeting_fstring)
print(line)
print()

# Exercise 5: Data for AI
user_id = 12345
username = "alice_data"
account_balance = 1250.75
is_premium = True
signup_year = 2023

current_year = 2024
years_member = current_year - signup_year
monthly_balance = account_balance / 12

print("Exercise 5:")
print(f"User {username} (ID: {user_id}) has been a member for {years_member} years")
print(f"Account balance: ${account_balance:.2f}")
print(f"Monthly balance: ${monthly_balance:.2f}")
print(f"Premium status: {is_premium}")
print()

# Bonus Challenge
sensor_id = 1001
temperature_c = 25.5
humidity = 65.2
timestamp = "2024-01-15 14:30:00"
is_anomaly = False

temperature_f = temperature_c * 9/5 + 32

print("Bonus Challenge:")
print(f"Sensor ID: {sensor_id}")
print(f"Temperature: {temperature_c}°C ({temperature_f:.1f}°F)")
print(f"Humidity: {humidity}%")
print(f"Timestamp: {timestamp}")
print(f"Anomaly detected: {is_anomaly}")
