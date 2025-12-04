"""
Day 4: Loops - Solutions
"""

# Exercise 1: Sum Calculator
total = 0
for i in range(1, 101):
    total += i
print(f"Sum of 1 to 100: {total}")

# Exercise 2: Data Processing
temperatures = [22.5, 25.0, 19.8, 23.2, 21.5, 24.0]
total = 0
for temp in temperatures:
    total += temp
average = total / len(temperatures)
print(f"Average temperature: {average:.2f}°C")

# Exercise 3: Pattern Finder
numbers = [1, 4, 7, 2, 9, 12, 15, 8, 20]
print("Even numbers:")
for num in numbers:
    if num % 2 == 0:
        print(num)

# Exercise 4: Validation Loop (commented out for non-interactive)
# while True:
#     age = int(input("Enter age (0-120): "))
#     if 0 <= age <= 120:
#         print(f"Valid age: {age}")
#         break
#     else:
#         print("Invalid! Try again.")

# Exercise 5: Data Aggregation
sensor_readings = [25.5, 26.0, 25.8, 100.0, 25.9, 26.1]
valid_readings = []
for reading in sensor_readings:
    if reading <= 50:  # Exclude anomalies
        valid_readings.append(reading)

if valid_readings:
    minimum = min(valid_readings)
    maximum = max(valid_readings)
    average = sum(valid_readings) / len(valid_readings)
    
    print(f"Valid readings: {len(valid_readings)}")
    print(f"Min: {minimum:.2f}")
    print(f"Max: {maximum:.2f}")
    print(f"Average: {average:.2f}")
