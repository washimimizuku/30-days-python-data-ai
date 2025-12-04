"""
Day 10: Mini Project - Data File Processor
Build a complete data file processor
"""

import csv
import json
from datetime import datetime

# Project: Build a data file processor that:
# 1. Reads sensor data from CSV
# 2. Validates and cleans the data
# 3. Calculates statistics
# 4. Exports results to JSON

# TODO: Create sample sensor data CSV
sample_data = """timestamp,sensor_id,temperature,humidity,status
2024-01-01 10:00:00,101,23.5,65.2,active
2024-01-01 10:05:00,102,invalid,62.8,active
2024-01-01 10:10:00,103,22.8,68.5,active
2024-01-01 10:15:00,101,24.1,64.5,error
2024-01-01 10:20:00,102,23.9,63.2,active"""

# TODO: Write to sensors_raw.csv


# TODO: Function to read CSV data
def read_sensor_data(filename):
    """Read sensor data from CSV file"""
    pass


# TODO: Function to validate data
def validate_reading(reading):
    """Validate a single sensor reading"""
    # Check temperature is float between -50 and 50
    # Check humidity is float between 0 and 100
    # Return True if valid, False otherwise
    pass


# TODO: Function to clean data
def clean_data(readings):
    """Remove invalid readings"""
    pass


# TODO: Function to calculate statistics
def calculate_stats(readings):
    """Calculate min, max, avg for temperature and humidity"""
    pass


# TODO: Function to export to JSON
def export_to_json(data, filename):
    """Export processed data to JSON"""
    pass


# TODO: Main processing pipeline
def main():
    # 1. Read data
    # 2. Clean data
    # 3. Calculate stats
    # 4. Export results
    pass


if __name__ == "__main__":
    main()
