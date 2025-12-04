# Day 26: Working with APIs - requests

## 📖 Learning Objectives
- Make HTTP requests (GET, POST)
- Handle JSON responses
- Work with query parameters
- Handle errors and timeouts
- Build API clients

## Theory

### Basic Requests
```python
import requests

# GET request
response = requests.get('https://api.example.com/data')

# Check status
if response.status_code == 200:
    data = response.json()
else:
    print(f"Error: {response.status_code}")
```

### Query Parameters
```python
# Method 1: URL string
url = 'https://api.example.com/search?q=python&limit=10'

# Method 2: params dict (preferred)
params = {'q': 'python', 'limit': 10}
response = requests.get('https://api.example.com/search', params=params)
```

### POST Requests
```python
data = {'name': 'Alice', 'age': 25}
response = requests.post('https://api.example.com/users', json=data)

if response.status_code == 201:
    new_user = response.json()
```

### Error Handling
```python
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()  # Raise exception for bad status
    data = response.json()
except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
```

### Headers and Authentication
```python
headers = {
    'Authorization': 'Bearer YOUR_TOKEN',
    'Content-Type': 'application/json'
}
response = requests.get(url, headers=headers)
```

## 💻 Exercises
Complete `exercise.py`

## Tomorrow: Day 27 - Async Programming
