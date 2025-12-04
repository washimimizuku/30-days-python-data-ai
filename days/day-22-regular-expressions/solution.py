"""
Day 22: Regular Expressions - Solutions
"""

import re

# Exercise 1
print("Exercise 1: Basic Pattern Matching")
text = "Contact us at support@example.com or call 555-123-4567"

# Search for pattern
email_match = re.search(r'\w+@\w+\.\w+', text)
if email_match:
    print(f"Found email: {email_match.group()}")

# Find all matches
emails = re.findall(r'\w+@\w+\.\w+', text)
print(f"All emails: {emails}")

# Phone numbers
phones = re.findall(r'\d{3}-\d{3}-\d{4}', text)
print(f"Phone numbers: {phones}")
print()

# Exercise 2
print("Exercise 2: Pattern Groups and Extraction")
log_entry = "2024-01-15 10:30:45 ERROR Database connection failed"

# Extract with groups
pattern = r'(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+) (.+)'
match = re.search(pattern, log_entry)

if match:
    date = match.group(1)
    time = match.group(2)
    level = match.group(3)
    message = match.group(4)
    
    print(f"Date: {date}")
    print(f"Time: {time}")
    print(f"Level: {level}")
    print(f"Message: {message}")

# Named groups
pattern_named = r'(?P<date>\d{4}-\d{2}-\d{2}) (?P<time>\d{2}:\d{2}:\d{2}) (?P<level>\w+) (?P<message>.+)'
match_named = re.search(pattern_named, log_entry)

if match_named:
    print(f"\nUsing named groups:")
    print(f"Date: {match_named.group('date')}")
    print(f"Level: {match_named.group('level')}")
print()

# Exercise 3
print("Exercise 3: Text Validation")

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def validate_phone(phone):
    pattern = r'^\d{3}-\d{3}-\d{4}$'
    return bool(re.match(pattern, phone))

def validate_sensor_id(sensor_id):
    pattern = r'^S\d{3}$'
    return bool(re.match(pattern, sensor_id))

# Test validations
test_emails = ["user@example.com", "invalid.email", "test@domain.co.uk"]
test_phones = ["555-123-4567", "5551234567", "555-12-34567"]
test_sensors = ["S001", "S999", "A001", "S12"]

print("Email validation:")
for email in test_emails:
    print(f"  {email}: {validate_email(email)}")

print("\nPhone validation:")
for phone in test_phones:
    print(f"  {phone}: {validate_phone(phone)}")

print("\nSensor ID validation:")
for sensor in test_sensors:
    print(f"  {sensor}: {validate_sensor_id(sensor)}")
print()

# Exercise 4
print("Exercise 4: Text Cleaning")

def clean_text(text):
    # Remove special characters, keep alphanumeric and spaces
    return re.sub(r'[^a-zA-Z0-9\s]', '', text)

def extract_numbers(text):
    return re.findall(r'\d+\.?\d*', text)

def clean_sensor_data(data_string):
    # Extract sensor ID and value
    pattern = r'Sensor_(\w+):\s*([\d.]+)'
    match = re.search(pattern, data_string)
    if match:
        return {"sensor_id": match.group(1), "value": float(match.group(2))}
    return None

# Test cleaning
dirty_text = "Hello! This is a test... #Python @2024"
print(f"Original: {dirty_text}")
print(f"Cleaned: {clean_text(dirty_text)}")

number_text = "Temperature: 23.5°C, Humidity: 65%, Pressure: 1013.25 hPa"
print(f"\nExtract numbers from: {number_text}")
print(f"Numbers: {extract_numbers(number_text)}")

sensor_string = "Sensor_A101: 23.5"
print(f"\nParse: {sensor_string}")
print(f"Result: {clean_sensor_data(sensor_string)}")
print()

# Exercise 5
print("Exercise 5: Log File Parsing")

log_data = """2024-01-15 10:00:00 INFO Application started
2024-01-15 10:05:23 WARNING High memory usage: 85%
2024-01-15 10:10:45 ERROR Database connection failed
2024-01-15 10:15:12 INFO Retry successful
2024-01-15 10:20:00 ERROR Timeout occurred after 30s"""

def parse_log_entry(entry):
    pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)'
    match = re.search(pattern, entry)
    if match:
        return {
            "timestamp": match.group(1),
            "level": match.group(2),
            "message": match.group(3)
        }
    return None

# Parse all log entries
log_entries = log_data.strip().split('\n')
parsed_logs = [parse_log_entry(entry) for entry in log_entries]

print("Parsed log entries:")
for log in parsed_logs:
    if log:
        print(f"  [{log['timestamp']}] {log['level']}: {log['message']}")

# Extract only errors
errors = [log for log in parsed_logs if log and log['level'] == 'ERROR']
print(f"\nFound {len(errors)} errors:")
for error in errors:
    print(f"  {error['timestamp']}: {error['message']}")
print()

# Bonus
print("Bonus: Complex Pattern Matching")

# Extract sensor readings from complex format
complex_data = """
Sensor readings for 2024-01-15:
- Sensor A (ID: S001) recorded 23.5°C at 10:00
- Sensor B (ID: S002) recorded 24.1°C at 10:05
- Sensor C (ID: S003) recorded 22.8°C at 10:10
"""

pattern = r'Sensor (\w+) \(ID: (S\d{3})\) recorded ([\d.]+)°C at (\d{2}:\d{2})'
matches = re.findall(pattern, complex_data)

print("Extracted sensor readings:")
for name, sensor_id, temp, time in matches:
    print(f"  {sensor_id} ({name}): {temp}°C at {time}")

# Replace patterns
cleaned = re.sub(r'\(ID: S\d{3}\)', '', complex_data)
print(f"\nRemoved sensor IDs from text")

print("\n" + "="*60)
print("Day 22 Complete! Move to Day 23")
print("="*60)
