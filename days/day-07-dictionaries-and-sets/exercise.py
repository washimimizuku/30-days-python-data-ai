"""
Day 7: Dictionaries and Sets - Exercises
Complete each exercise below
"""

# Exercise 1: User Data Management
# TODO: Create a dictionary for a user
user = {
    "id": 1001,
    "username": "alice_data",
    "email": "alice@example.com",
    "age": 25,
    "is_active": True
}

# TODO: Add a new field "role"


# TODO: Update the age to 26


# TODO: Print all keys


# TODO: Print all values


# TODO: Check if "email" exists in the dictionary


# Exercise 2: Word Frequency Counter
# TODO: Count word occurrences in this text
text = "python is great python is powerful python is easy"

# TODO: Split text into words
# words = ?

# TODO: Create a dictionary to count frequencies
# word_count = {}


# TODO: Print word frequencies


# Exercise 3: Remove Duplicates
# TODO: Given this list with duplicates
sensor_ids = [101, 102, 103, 101, 104, 102, 105, 103, 101]

# TODO: Use a set to get unique IDs
# unique_ids = ?

# TODO: Convert back to sorted list
# sorted_ids = ?


# Exercise 4: Data Lookup System
# TODO: Create a dictionary mapping sensor IDs to locations
sensor_locations = {
    101: "Building A - Floor 1",
    102: "Building A - Floor 2",
    103: "Building B - Floor 1",
    104: "Building B - Floor 2",
    105: "Building C - Floor 1"
}

# TODO: Look up location for sensor 103
# location = ?

# TODO: Safely look up sensor 999 (doesn't exist)
# location_999 = ?


# Exercise 5: Configuration Manager
# TODO: Create nested configuration dictionary
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

# TODO: Access database host
# db_host = ?

# TODO: Update API timeout to 60


# TODO: Add new section "logging"


# Bonus Challenge
# TODO: Merge two dictionaries
defaults = {"timeout": 30, "retries": 3, "debug": False}
user_config = {"timeout": 60, "debug": True}

# TODO: Merge (user_config should override defaults)
# final_config = ?
