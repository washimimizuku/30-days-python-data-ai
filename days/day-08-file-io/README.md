# Day 8: File I/O

## 📖 Learning Objectives (15 min)
- Read and write text files
- Use context managers (with statement)
- Handle file paths
- Process CSV files

## Theory

### Reading Files
```python
# Read entire file
with open("file.txt", "r") as f:
    content = f.read()

# Read lines
with open("file.txt", "r") as f:
    lines = f.readlines()

# Iterate over lines
with open("file.txt", "r") as f:
    for line in f:
        print(line.strip())
```

### Writing Files
```python
# Write (overwrites)
with open("file.txt", "w") as f:
    f.write("Hello, World!\n")

# Append
with open("file.txt", "a") as f:
    f.write("New line\n")
```

### CSV Files
```python
import csv

# Read CSV
with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["column_name"])

# Write CSV
with open("output.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age"])
    writer.writeheader()
    writer.writerow({"name": "Alice", "age": 25})
```

## 💻 Exercises (40 min)

### Exercise 1: Log File Reader
Read and parse log files

### Exercise 2: CSV Data Writer
Write data to CSV format

### Exercise 3: File Statistics
Calculate file statistics (lines, words, chars)

### Exercise 4: Data Format Converter
Convert between CSV and JSON

### Exercise 5: Batch File Processor
Process multiple files in a directory

## Tomorrow: Day 9 - Error Handling
