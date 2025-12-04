# Day 29: Testing with pytest

## 📖 Learning Objectives
- Write unit tests
- Use pytest fixtures
- Test with assertions
- Organize test files
- Measure test coverage

## Theory

### Basic Tests
```python
# test_calculator.py
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

# Run: pytest test_calculator.py
```

### Fixtures
```python
import pytest

@pytest.fixture
def sample_data():
    return [1, 2, 3, 4, 5]

def test_sum(sample_data):
    assert sum(sample_data) == 15

def test_len(sample_data):
    assert len(sample_data) == 5
```

### Testing Exceptions
```python
def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        result = 1 / 0
```

### Parametrized Tests
```python
@pytest.mark.parametrize("input,expected", [
    (2, 4),
    (3, 9),
    (4, 16),
])
def test_square(input, expected):
    assert input ** 2 == expected
```

## 💻 Exercises
Complete `exercise.py`

## Tomorrow: Day 30 - Capstone Project
