"""
Day 14: List Comprehensions - Solutions
"""

# Exercise 1
squares = [x**2 for x in range(1, 11)]
evens = [x for x in range(1, 21) if x % 2 == 0]

print("Exercise 1:")
print(f"Squares: {squares}")
print(f"Evens: {evens}")
print()

# Exercise 2
temperatures = [23.5, 26.1, 24.8, 27.3, 22.9, 28.1, 25.5]
hot_temps = [t for t in temperatures if t > 25]

sensors = [
    {"id": 101, "status": "active"},
    {"id": 102, "status": "inactive"},
    {"id": 103, "status": "active"}
]
active_ids = [s["id"] for s in sensors if s["status"] == "active"]

print("Exercise 2:")
print(f"Hot temperatures: {hot_temps}")
print(f"Active sensor IDs: {active_ids}")
print()

# Exercise 3
celsius_temps = [0, 10, 20, 30, 40]
fahrenheit_temps = [c * 9/5 + 32 for c in celsius_temps]

users = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}]
names = [u["name"] for u in users]

print("Exercise 3:")
print(f"Celsius: {celsius_temps}")
print(f"Fahrenheit: {fahrenheit_temps}")
print(f"Names: {names}")
print()

# Exercise 4
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]

table = [[i * j for j in range(1, 6)] for i in range(1, 6)]

print("Exercise 4:")
print(f"Matrix: {matrix}")
print(f"Flattened: {flat}")
print(f"Multiplication table (5x5):")
for row in table:
    print(f"  {row}")
print()

# Exercise 5
squares_dict = {x: x**2 for x in range(1, 11)}

data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique = {x for x in data}

print("Exercise 5:")
print(f"Squares dict: {squares_dict}")
print(f"Original data: {data}")
print(f"Unique values: {unique}")
print()

# Bonus: Complex transformation
sensor_readings = [
    {"sensor_id": 101, "temp": 23.5, "humidity": 65},
    {"sensor_id": 102, "temp": 26.1, "humidity": 58},
    {"sensor_id": 103, "temp": 24.8, "humidity": 62},
    {"sensor_id": 104, "temp": 27.3, "humidity": 55}
]

# Filter, transform, and create summary
hot_sensors = [
    {
        "id": r["sensor_id"],
        "temp_f": round(r["temp"] * 9/5 + 32, 1),
        "comfort": "low" if r["humidity"] < 60 else "high"
    }
    for r in sensor_readings
    if r["temp"] > 25
]

print("Bonus:")
print("Hot sensors (>25°C) with comfort level:")
for sensor in hot_sensors:
    print(f"  Sensor {sensor['id']}: {sensor['temp_f']}°F, Comfort: {sensor['comfort']}")
