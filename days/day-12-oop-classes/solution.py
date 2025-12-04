"""
Day 12: OOP - Classes - Solutions
"""

import random
from datetime import datetime

# Exercise 1
class Sensor:
    def __init__(self, sensor_id, location):
        self.sensor_id = sensor_id
        self.location = location
        self.is_active = True
    
    def read_temperature(self):
        if self.is_active:
            return round(random.uniform(20, 30), 1)
        return None
    
    def get_info(self):
        return f"Sensor {self.sensor_id} at {self.location}"

print("Exercise 1:")
sensor1 = Sensor(101, "Building A")
print(sensor1.get_info())
print(f"Temperature: {sensor1.read_temperature()}°C")
print()

# Exercise 2
class DataPoint:
    def __init__(self, sensor_id, value, timestamp=None):
        self.sensor_id = sensor_id
        self.value = value
        self.timestamp = timestamp or datetime.now()
    
    def __str__(self):
        return f"[{self.timestamp}] Sensor {self.sensor_id}: {self.value}"

print("Exercise 2:")
dp = DataPoint(101, 23.5)
print(dp)
print()

# Exercise 3
class DataLogger:
    def __init__(self):
        self.data_points = []
    
    def log(self, data_point):
        self.data_points.append(data_point)
    
    def get_count(self):
        return len(self.data_points)
    
    def get_average(self):
        if not self.data_points:
            return 0
        return sum(dp.value for dp in self.data_points) / len(self.data_points)

print("Exercise 3:")
logger = DataLogger()
logger.log(DataPoint(101, 23.5))
logger.log(DataPoint(101, 24.1))
logger.log(DataPoint(101, 23.8))
print(f"Logged {logger.get_count()} points")
print(f"Average: {logger.get_average():.2f}")
print()

# Exercise 4
print("Exercise 4:")
sensors = [
    Sensor(101, "Building A"),
    Sensor(102, "Building B"),
    Sensor(103, "Building C")
]

logger = DataLogger()
for sensor in sensors:
    temp = sensor.read_temperature()
    logger.log(DataPoint(sensor.sensor_id, temp))
    print(f"{sensor.get_info()}: {temp}°C")

print(f"\nTotal readings: {logger.get_count()}")
print(f"Average temperature: {logger.get_average():.2f}°C")
print()

# Exercise 5
class AdvancedSensor:
    sensor_count = 0  # Class variable
    
    def __init__(self, sensor_id, location):
        self.sensor_id = sensor_id
        self.location = location
        self._temperature = 25.0  # Private attribute
        AdvancedSensor.sensor_count += 1
    
    @property
    def temperature(self):
        """Property to get temperature"""
        return self._temperature
    
    @temperature.setter
    def temperature(self, value):
        """Property to set temperature with validation"""
        if -50 <= value <= 50:
            self._temperature = value
        else:
            raise ValueError("Temperature out of range")
    
    @classmethod
    def get_sensor_count(cls):
        """Class method to get total sensor count"""
        return cls.sensor_count
    
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        """Static method for temperature conversion"""
        return celsius * 9/5 + 32

print("Exercise 5:")
s1 = AdvancedSensor(201, "Lab 1")
s2 = AdvancedSensor(202, "Lab 2")

print(f"Temperature: {s1.temperature}°C")
s1.temperature = 28.5
print(f"Updated: {s1.temperature}°C")
print(f"In Fahrenheit: {AdvancedSensor.celsius_to_fahrenheit(s1.temperature):.1f}°F")
print(f"Total sensors created: {AdvancedSensor.get_sensor_count()}")
print()

# Bonus
class SensorNetwork:
    def __init__(self, name):
        self.name = name
        self.sensors = []
    
    def add_sensor(self, sensor):
        self.sensors.append(sensor)
    
    def read_all(self):
        readings = {}
        for sensor in self.sensors:
            readings[sensor.sensor_id] = sensor.read_temperature()
        return readings
    
    def get_stats(self):
        readings = list(self.read_all().values())
        readings = [r for r in readings if r is not None]
        if not readings:
            return {}
        return {
            "min": min(readings),
            "max": max(readings),
            "avg": sum(readings) / len(readings)
        }

print("Bonus:")
network = SensorNetwork("Campus Network")
network.add_sensor(Sensor(301, "Building A"))
network.add_sensor(Sensor(302, "Building B"))
network.add_sensor(Sensor(303, "Building C"))

readings = network.read_all()
print(f"Network: {network.name}")
print(f"Readings: {readings}")
stats = network.get_stats()
print(f"Stats: Min={stats['min']:.1f}, Max={stats['max']:.1f}, Avg={stats['avg']:.1f}")
