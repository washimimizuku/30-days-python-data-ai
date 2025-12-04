# Day 22: Regular Expressions

## 📖 Learning Objectives
- Understand regex patterns
- Match and search text
- Extract data with groups
- Validate input formats
- Clean and parse text data

## Theory

### Basic Patterns
```python
import re

# Search for pattern
match = re.search(r'\d+', 'Order 12345')  # Finds '12345'

# Find all matches
numbers = re.findall(r'\d+', 'Call 555-1234 or 555-5678')

# Match from start
if re.match(r'\d{3}', '123abc'):
    print("Starts with 3 digits")
```

### Common Patterns
```
\d    - Digit [0-9]
\w    - Word character [a-zA-Z0-9_]
\s    - Whitespace
.     - Any character
*     - 0 or more
+     - 1 or more
?     - 0 or 1
{n}   - Exactly n times
[abc] - Any of a, b, or c
^     - Start of string
$     - End of string
```

### Groups and Extraction
```python
# Extract with groups
pattern = r'(\d{4})-(\d{2})-(\d{2})'
match = re.search(pattern, '2024-01-15')
year, month, day = match.groups()

# Named groups
pattern = r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})'
match = re.search(pattern, '2024-01-15')
print(match.group('year'))  # '2024'
```

### Validation
```python
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def validate_phone(phone):
    pattern = r'^\d{3}-\d{3}-\d{4}$'
    return bool(re.match(pattern, phone))
```

## 💻 Exercises
Complete `exercise.py`

## Tomorrow: Day 23 - Virtual Environments
