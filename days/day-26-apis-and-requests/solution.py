"""
Day 26: Working with APIs - requests library - Solutions
"""

import requests
import json

print("="*60)
print("Day 26: Working with APIs")
print("="*60)
print()

# Exercise 1
print("Exercise 1: Basic GET Request")
print("""
# Make GET request
response = requests.get('https://api.example.com/data')

# Check status
if response.status_code == 200:
    print("Success!")
    data = response.json()
else:
    print(f"Error: {response.status_code}")

# Common status codes:
# 200: OK
# 404: Not Found
# 500: Server Error
""")

# Exercise 2
print("Exercise 2: Handle JSON Response")
print("""
# Example with JSONPlaceholder (free test API)
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
data = response.json()

print(data['title'])
print(data['body'])

# Access nested data
user_id = data['userId']
""")

# Exercise 3
print("Exercise 3: Query Parameters")
print("""
# Method 1: URL string
url = 'https://api.example.com/search?q=python&limit=10'
response = requests.get(url)

# Method 2: params dict (preferred)
params = {
    'q': 'python',
    'limit': 10,
    'sort': 'date'
}
response = requests.get('https://api.example.com/search', params=params)
""")

# Exercise 4
print("Exercise 4: POST Requests")
print("""
# Send JSON data
data = {
    'title': 'New Post',
    'body': 'Content here',
    'userId': 1
}

response = requests.post(
    'https://api.example.com/posts',
    json=data
)

if response.status_code == 201:
    print("Created!")
    new_item = response.json()
""")

# Exercise 5
print("Exercise 5: Error Handling")

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
    
    def get(self, endpoint, params=None):
        """Make GET request with error handling"""
        try:
            url = f"{self.base_url}/{endpoint}"
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.Timeout:
            print("Request timed out")
            return None
        except requests.exceptions.HTTPError as e:
            print(f"HTTP Error: {e}")
            return None
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None
    
    def post(self, endpoint, data):
        """Make POST request with error handling"""
        try:
            url = f"{self.base_url}/{endpoint}"
            response = self.session.post(url, json=data, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None

# Demo usage
print("\nAPI Client Example:")
client = APIClient("https://jsonplaceholder.typicode.com")

# GET request
post = client.get("posts/1")
if post:
    print(f"Title: {post.get('title', 'N/A')}")

# POST request
new_post = {
    "title": "Test Post",
    "body": "This is a test",
    "userId": 1
}
result = client.post("posts", new_post)
if result:
    print(f"Created post with ID: {result.get('id', 'N/A')}")

print("\n" + "="*60)
print("Day 26 Complete! Move to Day 27")
print("="*60)
