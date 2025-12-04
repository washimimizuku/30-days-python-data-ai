# Day 19: Working with CSV and JSON

## 📖 Learning Objectives
- Read and write CSV files
- Handle different CSV formats
- Work with JSON data
- Convert between formats
- Handle nested JSON structures

## Theory

### CSV Operations
```python
# Read CSV
df = pd.read_csv('data.csv')
df = pd.read_csv('data.csv', delimiter=';')  # Different delimiter
df = pd.read_csv('data.csv', na_values=['NA', 'missing'])

# Write CSV
df.to_csv('output.csv', index=False)
df.to_csv('output.csv', columns=['col1', 'col2'])
```

### JSON Operations
```python
# Read JSON
df = pd.read_json('data.json')
with open('data.json') as f:
    data = json.load(f)

# Write JSON
df.to_json('output.json', orient='records', indent=2)
with open('output.json', 'w') as f:
    json.dump(data, f, indent=2)
```

### Format Conversion
```python
# CSV to JSON
df = pd.read_csv('data.csv')
df.to_json('data.json', orient='records')

# JSON to CSV
df = pd.read_json('data.json')
df.to_csv('data.csv', index=False)
```

## 💻 Exercises
Complete `exercise.py`

## Tomorrow: Day 20 - Mini Project
