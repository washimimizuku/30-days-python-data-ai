"""
Day 29: Testing with pytest - Solutions
"""

print("="*60)
print("Day 29: Testing with pytest")
print("="*60)
print()

# Exercise 1
print("Exercise 1: Basic Test Functions")
print("""
# test_basic.py
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

# Run with: pytest test_basic.py
""")

# Exercise 2
print("Exercise 2: Test with Assertions")

def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def test_calculate_average():
    # Test normal case
    assert calculate_average([1, 2, 3, 4, 5]) == 3.0
    
    # Test empty list
    assert calculate_average([]) == 0
    
    # Test single value
    assert calculate_average([10]) == 10
    
    # Test negative numbers
    assert calculate_average([-1, -2, -3]) == -2.0

print("✓ test_calculate_average would pass")
print()

# Exercise 3
print("Exercise 3: Test Fixtures")
print("""
# test_with_fixtures.py
import pytest

@pytest.fixture
def sample_data():
    return [23.5, 24.1, 23.8, 25.0, 24.5]

@pytest.fixture
def sensor_config():
    return {
        'sensor_id': 101,
        'location': 'Building A',
        'type': 'temperature'
    }

def test_with_fixture(sample_data):
    assert len(sample_data) == 5
    assert min(sample_data) == 23.5
    assert max(sample_data) == 25.0

def test_sensor_config(sensor_config):
    assert sensor_config['sensor_id'] == 101
    assert 'location' in sensor_config
""")

# Exercise 4
print("Exercise 4: Test Data Processing")

def clean_sensor_data(readings):
    """Remove outliers and invalid values"""
    if not readings:
        return []
    
    # Remove None values
    valid = [r for r in readings if r is not None]
    
    # Remove outliers using IQR method
    if len(valid) < 4:
        return valid
    
    sorted_data = sorted(valid)
    n = len(sorted_data)
    q1 = sorted_data[n // 4]
    q3 = sorted_data[3 * n // 4]
    iqr = q3 - q1
    
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    
    cleaned = [r for r in valid if lower_bound <= r <= upper_bound]
    return cleaned

def test_clean_sensor_data():
    # Test with normal data
    data = [23, 24, 25, 24, 23]
    result = clean_sensor_data(data)
    assert len(result) == 5
    
    # Test with outlier
    data_with_outlier = [23, 24, 25, 100, 24]
    result = clean_sensor_data(data_with_outlier)
    assert 100 not in result
    
    # Test with None values
    data_with_none = [23, None, 24, 25]
    result = clean_sensor_data(data_with_none)
    assert None not in result
    assert len(result) == 3
    
    # Test empty list
    assert clean_sensor_data([]) == []

print("Running tests...")
test_clean_sensor_data()
print("✓ All tests passed")
print()

# Exercise 5
print("Exercise 5: Complete Test Suite")
print("""
# test_sensor_module.py
import pytest

class SensorData:
    def __init__(self, sensor_id, readings):
        self.sensor_id = sensor_id
        self.readings = readings
    
    def get_average(self):
        if not self.readings:
            return 0
        return sum(self.readings) / len(self.readings)
    
    def get_min_max(self):
        if not self.readings:
            return None, None
        return min(self.readings), max(self.readings)

class TestSensorData:
    @pytest.fixture
    def sensor(self):
        return SensorData(101, [23.5, 24.1, 23.8, 25.0])
    
    def test_initialization(self, sensor):
        assert sensor.sensor_id == 101
        assert len(sensor.readings) == 4
    
    def test_get_average(self, sensor):
        avg = sensor.get_average()
        assert abs(avg - 24.1) < 0.01
    
    def test_get_min_max(self, sensor):
        min_val, max_val = sensor.get_min_max()
        assert min_val == 23.5
        assert max_val == 25.0
    
    def test_empty_readings(self):
        empty_sensor = SensorData(102, [])
        assert empty_sensor.get_average() == 0
        assert empty_sensor.get_min_max() == (None, None)

# Run with: pytest test_sensor_module.py -v
""")

# Bonus
print("Bonus: Parametrized Tests")
print("""
import pytest

@pytest.mark.parametrize("input,expected", [
    ([1, 2, 3], 2.0),
    ([10], 10.0),
    ([5, 5, 5], 5.0),
    ([-1, 0, 1], 0.0),
])
def test_average_parametrized(input, expected):
    assert calculate_average(input) == expected

# This runs 4 separate tests with different inputs!
""")

print("\n" + "="*60)
print("Day 29 Complete! Move to Day 30 - Final Capstone!")
print("="*60)
