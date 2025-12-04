"""
Day 10: Mini Project - Data File Processor - Solution
"""

import csv
import json
from datetime import datetime
import os

# Create sample data
os.makedirs("data/raw", exist_ok=True)
os.makedirs("data/processed", exist_ok=True)

sample_data = """timestamp,sensor_id,temperature,humidity,status
2024-01-01 10:00:00,101,23.5,65.2,active
2024-01-01 10:05:00,102,invalid,62.8,active
2024-01-01 10:10:00,103,22.8,68.5,active
2024-01-01 10:15:00,101,24.1,64.5,error
2024-01-01 10:20:00,102,23.9,63.2,active"""

with open("data/raw/sensors_raw.csv", "w") as f:
    f.write(sample_data)

def read_sensor_data(filename):
    """Read sensor data from CSV file"""
    readings = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            readings.append(row)
    return readings

def validate_reading(reading):
    """Validate a single sensor reading"""
    try:
        temp = float(reading["temperature"])
        humidity = float(reading["humidity"])
        
        if not (-50 <= temp <= 50):
            return False
        if not (0 <= humidity <= 100):
            return False
        
        return True
    except (ValueError, KeyError):
        return False

def clean_data(readings):
    """Remove invalid readings"""
    valid_readings = []
    for reading in readings:
        if validate_reading(reading):
            valid_readings.append(reading)
    return valid_readings

def calculate_stats(readings):
    """Calculate statistics"""
    if not readings:
        return {}
    
    temps = [float(r["temperature"]) for r in readings]
    humidities = [float(r["humidity"]) for r in readings]
    
    stats = {
        "total_readings": len(readings),
        "temperature": {
            "min": min(temps),
            "max": max(temps),
            "avg": sum(temps) / len(temps)
        },
        "humidity": {
            "min": min(humidities),
            "max": max(humidities),
            "avg": sum(humidities) / len(humidities)
        }
    }
    return stats

def export_to_json(data, filename):
    """Export to JSON"""
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

def main():
    print("=== Data File Processor ===\n")
    
    # Read data
    print("1. Reading data...")
    raw_data = read_sensor_data("data/raw/sensors_raw.csv")
    print(f"   Read {len(raw_data)} readings")
    
    # Clean data
    print("2. Cleaning data...")
    clean_readings = clean_data(raw_data)
    print(f"   {len(clean_readings)} valid readings")
    print(f"   {len(raw_data) - len(clean_readings)} invalid readings removed")
    
    # Calculate stats
    print("3. Calculating statistics...")
    stats = calculate_stats(clean_readings)
    print(f"   Temperature: {stats['temperature']['avg']:.1f}°C avg")
    print(f"   Humidity: {stats['humidity']['avg']:.1f}% avg")
    
    # Export
    print("4. Exporting results...")
    results = {
        "processed_at": datetime.now().isoformat(),
        "statistics": stats,
        "clean_data": clean_readings
    }
    export_to_json(results, "data/processed/sensor_results.json")
    print("   Exported to data/processed/sensor_results.json")
    
    print("\n✅ Processing complete!")
    
    # Cleanup
    if os.path.exists("data/raw/sensors_raw.csv"):
        os.remove("data/raw/sensors_raw.csv")
    if os.path.exists("data/processed/sensor_results.json"):
        os.remove("data/processed/sensor_results.json")

if __name__ == "__main__":
    main()
