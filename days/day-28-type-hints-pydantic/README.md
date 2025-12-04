# Day 28: Type Hints and Pydantic

## 📖 Learning Objectives
- Add type hints to functions
- Use complex types (List, Dict, Optional)
- Validate data with Pydantic
- Create data models
- Improve code quality

## Theory

### Basic Type Hints
```python
def greet(name: str) -> str:
    return f"Hello, {name}"

def add(a: int, b: int) -> int:
    return a + b

age: int = 25
name: str = "Alice"
```

### Complex Types
```python
from typing import List, Dict, Optional, Union

def process_data(
    values: List[float],
    config: Dict[str, any],
    threshold: Optional[float] = None
) -> List[float]:
    pass
```

### Pydantic Models
```python
from pydantic import BaseModel, validator

class SensorReading(BaseModel):
    sensor_id: int
    temperature: float
    humidity: float
    
    @validator('temperature')
    def validate_temp(cls, v):
        if not -50 <= v <= 50:
            raise ValueError('Invalid temperature')
        return v

# Automatic validation
reading = SensorReading(
    sensor_id=101,
    temperature=23.5,
    humidity=65.0
)
```

## 💻 Exercises
Complete `exercise.py`

## Tomorrow: Day 29 - Testing with pytest
