"""
Day 7: Dictionaries and Sets - Solutions
"""

# Exercise 1: User Data Management
user = {
    "id": 1001,
    "username": "alice_data",
    "email": "alice@example.com",
    "age": 25,
    "is_active": True
}

user["role"] = "data_engineer"
user["age"] = 26

print("Exercise 1:")
print(f"Keys: {list(user.keys())}")
print(f"Values: {list(user.values())}")
print(f"Has email: {'email' in user}")
print(f"User: {user}")
print()

# Exercise 2: Word Frequency Counter
text = "python is great python is powerful python is easy"
words = text.split()

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Alternative: word_count[word] = word_count.get(word, 0) + 1

print("Exercise 2:")
print(f"Text: {text}")
print(f"Word frequencies: {word_count}")
print()

# Exercise 3: Remove Duplicates
sensor_ids = [101, 102, 103, 101, 104, 102, 105, 103, 101]
unique_ids = set(sensor_ids)
sorted_ids = sorted(list(unique_ids))

print("Exercise 3:")
print(f"Original: {sensor_ids}")
print(f"Unique: {unique_ids}")
print(f"Sorted unique: {sorted_ids}")
print()

# Exercise 4: Data Lookup System
sensor_locations = {
    101: "Building A - Floor 1",
    102: "Building A - Floor 2",
    103: "Building B - Floor 1",
    104: "Building B - Floor 2",
    105: "Building C - Floor 1"
}

location = sensor_locations[103]
location_999 = sensor_locations.get(999, "Unknown location")

print("Exercise 4:")
print(f"Sensor 103 location: {location}")
print(f"Sensor 999 location: {location_999}")
print()

# Exercise 5: Configuration Manager
config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "datadb"
    },
    "api": {
        "endpoint": "https://api.example.com",
        "timeout": 30
    }
}

db_host = config["database"]["host"]
config["api"]["timeout"] = 60
config["logging"] = {"level": "INFO", "file": "app.log"}

print("Exercise 5:")
print(f"Database host: {db_host}")
print(f"Updated config: {config}")
print()

# Bonus Challenge
defaults = {"timeout": 30, "retries": 3, "debug": False}
user_config = {"timeout": 60, "debug": True}

final_config = {**defaults, **user_config}
# Alternative: defaults.copy() then update()

print("Bonus Challenge:")
print(f"Defaults: {defaults}")
print(f"User config: {user_config}")
print(f"Final config: {final_config}")
