"""
Day 13: OOP - Inheritance - Solutions
"""

from abc import ABC, abstractmethod
import random

# Exercise 1
class Device:
    def __init__(self, device_id, name):
        self.device_id = device_id
        self.name = name
        self.is_online = True
    
    def get_status(self):
        return "online" if self.is_online else "offline"

class Sensor(Device):
    def __init__(self, device_id, name, sensor_type):
        super().__init__(device_id, name)
        self.sensor_type = sensor_type
    
    def read(self):
        return round(random.uniform(20, 30), 1)

class Actuator(Device):
    def __init__(self, device_id, name):
        super().__init__(device_id, name)
        self.state = "off"
    
    def turn_on(self):
        self.state = "on"
    
    def turn_off(self):
        self.state = "off"

print("Exercise 1:")
sensor = Sensor(101, "Temp Sensor", "temperature")
actuator = Actuator(201, "Fan")
print(f"Sensor: {sensor.name}, Status: {sensor.get_status()}")
print(f"Actuator: {actuator.name}, State: {actuator.state}")
print()

# Exercise 2
class ImprovedSensor(Device):
    def __init__(self, device_id, name, sensor_type):
        super().__init__(device_id, name)
        self.sensor_type = sensor_type
    
    def __str__(self):
        return f"{self.sensor_type.title()} Sensor '{self.name}' (ID: {self.device_id})"
    
    def read(self):
        return round(random.uniform(20, 30), 1)

print("Exercise 2:")
sensor = ImprovedSensor(101, "Room Temp", "temperature")
print(sensor)
print()

# Exercise 3
class SmartDevice(Device):
    def __init__(self, device_id, name, firmware_version):
        super().__init__(device_id, name)
        self.firmware_version = firmware_version
    
    def get_status(self):
        base_status = super().get_status()
        return f"{base_status} (firmware: {self.firmware_version})"

class SmartSensor(SmartDevice):
    def __init__(self, device_id, name, firmware_version, sensor_type):
        super().__init__(device_id, name, firmware_version)
        self.sensor_type = sensor_type

print("Exercise 3:")
smart_sensor = SmartSensor(301, "Smart Temp", "v2.1", "temperature")
print(f"Status: {smart_sensor.get_status()}")
print()

# Exercise 4
class Loggable:
    def log(self, message):
        print(f"[LOG] {message}")

class Alertable:
    def send_alert(self, message):
        print(f"[ALERT] {message}")

class MonitoringSensor(Sensor, Loggable, Alertable):
    def __init__(self, device_id, name, sensor_type, threshold):
        super().__init__(device_id, name, sensor_type)
        self.threshold = threshold
    
    def read(self):
        value = super().read()
        self.log(f"Reading: {value}")
        if value > self.threshold:
            self.send_alert(f"Value {value} exceeds threshold {self.threshold}")
        return value

print("Exercise 4:")
monitor = MonitoringSensor(401, "Critical Temp", "temperature", 25)
monitor.read()
print()

# Exercise 5
class DataSource(ABC):
    @abstractmethod
    def read_data(self):
        pass
    
    @abstractmethod
    def validate_data(self, data):
        pass

class TemperatureSensor(DataSource):
    def __init__(self, sensor_id):
        self.sensor_id = sensor_id
    
    def read_data(self):
        return round(random.uniform(20, 30), 1)
    
    def validate_data(self, data):
        return -50 <= data <= 50

class HumiditySensor(DataSource):
    def __init__(self, sensor_id):
        self.sensor_id = sensor_id
    
    def read_data(self):
        return round(random.uniform(40, 80), 1)
    
    def validate_data(self, data):
        return 0 <= data <= 100

print("Exercise 5:")
temp_sensor = TemperatureSensor(501)
humidity_sensor = HumiditySensor(502)

temp = temp_sensor.read_data()
print(f"Temperature: {temp}°C, Valid: {temp_sensor.validate_data(temp)}")

humidity = humidity_sensor.read_data()
print(f"Humidity: {humidity}%, Valid: {humidity_sensor.validate_data(humidity)}")
print()

# Bonus
class IoTDevice(ABC):
    def __init__(self, device_id, name, location):
        self.device_id = device_id
        self.name = name
        self.location = location
        self.is_online = True
    
    @abstractmethod
    def get_data(self):
        pass
    
    def __str__(self):
        return f"{self.__class__.__name__} '{self.name}' at {self.location}"

class TemperatureDevice(IoTDevice):
    def get_data(self):
        return {"type": "temperature", "value": round(random.uniform(20, 30), 1), "unit": "°C"}

class HumidityDevice(IoTDevice):
    def get_data(self):
        return {"type": "humidity", "value": round(random.uniform(40, 80), 1), "unit": "%"}

class MultiSensor(IoTDevice):
    def get_data(self):
        return {
            "temperature": round(random.uniform(20, 30), 1),
            "humidity": round(random.uniform(40, 80), 1),
            "pressure": round(random.uniform(980, 1020), 1)
        }

print("Bonus:")
devices = [
    TemperatureDevice(601, "Temp-01", "Room A"),
    HumidityDevice(602, "Humid-01", "Room B"),
    MultiSensor(603, "Multi-01", "Room C")
]

for device in devices:
    print(device)
    print(f"  Data: {device.get_data()}")
