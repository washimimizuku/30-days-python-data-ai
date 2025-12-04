# Day 10: Mini Project - Data File Processor

## 📖 Project Overview (60 min)

Build a complete data file processor that demonstrates all skills from Week 1.

## Project Requirements

### Input
CSV file with sensor data:
```csv
timestamp,sensor_id,temperature,humidity,pressure
2024-01-01 10:00:00,S001,25.5,65.2,1013.25
2024-01-01 10:01:00,S001,150.0,65.5,1013.30
2024-01-01 10:02:00,S002,26.0,64.8,1013.20
```

### Tasks
1. **Read CSV file**
2. **Validate each record**:
   - Temperature: -50 to 50°C
   - Humidity: 0 to 100%
   - Pressure: 900 to 1100 hPa
3. **Clean data**: Remove invalid records
4. **Calculate statistics**:
   - Count: total, valid, invalid
   - Temperature: min, max, average
   - Humidity: min, max, average
5. **Write outputs**:
   - `cleaned_data.csv` - Valid records only
   - `summary_report.txt` - Statistics
   - `errors.log` - Invalid records

### Example Output (summary_report.txt)
```
Data Processing Summary
=======================
Total records: 100
Valid records: 95
Invalid records: 5

Temperature Statistics:
  Min: 18.5°C
  Max: 32.1°C
  Average: 25.3°C

Humidity Statistics:
  Min: 45.2%
  Max: 78.9%
  Average: 62.1%
```

## Skills Demonstrated
- File I/O (reading/writing CSV)
- Data validation
- Error handling
- Functions
- Lists and dictionaries
- String formatting
- Control flow

## Starter Code

See `exercise.py` for template

## Bonus Challenges
1. Add command-line arguments for input/output files
2. Support multiple sensor types with different ranges
3. Generate charts with matplotlib
4. Add logging instead of print statements

## Next Week
Week 2: Object-Oriented Programming and List Comprehensions
