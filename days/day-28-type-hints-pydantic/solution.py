"""
Day 28: Type Hints and Pydantic - Solutions
"""

from typing import List, Dict, Optional, Union, Tuple
from datetime import datetime

print("="*60)
print("Day 28: Type Hints and Pydantic")
print("="*60)
print()

# Exercise 1
print("Exercise 1: Basic Type Hints")

def add_numbers(a: int, b: int) -> int:
    return a + b

def greet(name: str) -> str:
    return f"Hello, {name}!"

def calculate_average(numbers: List[float]) -> float:
    return sum(numbers) / len(numbers)

print(f"add_numbers(5, 3) = {add_numbers(5, 3)}")
print(f"greet('Alice') = {greet('Alice')}")
print(f"calculate_average([1, 2, 3, 4, 5]) = {calculate_average([1, 2, 3, 4, 5])}")
print()

# Exercise 2
print("Exercise 2: Complex Types")

def process_sensor_data(
    sensor_id: int,
    readings: List[float],
    metadata: Optional[Dict[str, str]] = None
) -> Dict[str, Union[int, float, str]]:
    result = {
        "sensor_id": sensor_id,
        "count": len(readings),
        "average": sum(readings) / len(readings),
        "min": min(readings),
        "max": max(readings)
    }
    if metadata:
        result["location"] = metadata.get("location", "unknown")
    return result

readings = [23.5, 24.1, 23.8, 25.0]
metadata = {"location": "Building A"}
result = process_sensor_data(101, readings, metadata)
print(f"Sensor data processed: {result}")
print()

# Exercise 3
print("Exercise 3: Pydantic Models")

try:
    from pydantic import BaseModel, Field, field_validator
    
    class SensorReading(BaseModel):
        sensor_id: int
        temperature: float
        humidity: float
        timestamp: datetime
        location: Optional[str] = None
        
        @field_validator('temperature')
        @classmethod
        def validate_temperature(cls, v):
            if not -50 <= v <= 50:
                raise ValueError('Temperature must be between -50 and 50')
            return v
        
        @field_validator('humidity')
        @classmethod
        def validate_humidity(cls, v):
            if not 0 <= v <= 100:
                raise ValueError('Humidity must be between 0 and 100')
            return v
    
    # Valid reading
    reading = SensorReading(
        sensor_id=101,
        temperature=23.5,
        humidity=65.2,
        timestamp=datetime.now(),
        location="Building A"
    )
    print(f"Valid reading: {reading}")
    print(f"As dict: {reading.model_dump()}")
    print(f"As JSON: {reading.model_dump_json()}")
    
    # Invalid reading (will raise error)
    try:
        invalid = SensorReading(
            sensor_id=102,
            temperature=100,  # Invalid!
            humidity=65,
            timestamp=datetime.now()
        )
    except Exception as e:
        print(f"\nValidation error: {e}")
    
    print()
    
except ImportError:
    print("Pydantic not installed. Install with: pip install pydantic")
    print()

# Exercise 4
print("Exercise 4: Data Validation with Type Hints")

def validate_sensor_config(config: Dict[str, any]) -> Tuple[bool, Optional[str]]:
    """Validate sensor configuration"""
    required_fields = ['sensor_id', 'type', 'location']
    
    for field in required_fields:
        if field not in config:
            return False, f"Missing required field: {field}"
    
    if not isinstance(config['sensor_id'], int):
        return False, "sensor_id must be an integer"
    
    if config['type'] not in ['temperature', 'humidity', 'pressure']:
        return False, "Invalid sensor type"
    
    return True, None

# Test validation
configs = [
    {'sensor_id': 101, 'type': 'temperature', 'location': 'Room A'},
    {'sensor_id': '102', 'type': 'humidity', 'location': 'Room B'},
    {'type': 'pressure', 'location': 'Room C'}
]

for i, config in enumerate(configs, 1):
    valid, error = validate_sensor_config(config)
    if valid:
        print(f"Config {i}: ✓ Valid")
    else:
        print(f"Config {i}: ✗ {error}")
print()

# Exercise 5
print("Exercise 5: API Models")

try:
    from pydantic import BaseModel
    
    from pydantic import ConfigDict
    
    class SensorCreateRequest(BaseModel):
        model_config = ConfigDict(
            json_schema_extra={
                "example": {
                    "sensor_id": 101,
                    "type": "temperature",
                    "location": "Building A"
                }
            }
        )
        
        sensor_id: int
        type: str
        location: str
    
    class SensorResponse(BaseModel):
        sensor_id: int
        type: str
        location: str
        status: str = "active"
        created_at: datetime
    
    # Simulate API request
    request_data = {
        "sensor_id": 101,
        "type": "temperature",
        "location": "Building A"
    }
    
    request = SensorCreateRequest(**request_data)
    print(f"Request: {request}")
    
    # Simulate API response
    response = SensorResponse(
        **request.model_dump(),
        created_at=datetime.now()
    )
    print(f"Response: {response.model_dump_json(indent=2)}")
    
except ImportError:
    print("Pydantic not installed")

print("\n" + "="*60)
print("Day 28 Complete! Move to Day 29")
print("="*60)
