# Day 13: OOP - Inheritance and Methods

## 📖 Learning Objectives (15 min)
- Understand inheritance
- Override methods
- Use super()
- Implement polymorphism

## Theory

### Inheritance
```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"
```

### Using super()
```python
class Sensor:
    def __init__(self, id):
        self.id = id

class TemperatureSensor(Sensor):
    def __init__(self, id, unit="C"):
        super().__init__(id)
        self.unit = unit
```

## 💻 Exercises (40 min)

### Exercise 1: Sensor Hierarchy
Create TemperatureSensor, HumiditySensor classes

### Exercise 2: Data Processor Inheritance
Base processor with specialized processors

### Exercise 3: Shape Classes
Circle, Rectangle inheriting from Shape

### Exercise 4: User Roles
Admin, User, Guest with different permissions

### Exercise 5: Vehicle Hierarchy
Car, Truck, Motorcycle from Vehicle

## Tomorrow: Day 14 - List Comprehensions
