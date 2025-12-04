# Day 13 Quiz: OOP - Inheritance

## Questions

### 1. What is inheritance in OOP?

**Your answer:**


**Correct answer:** Inheritance allows a class (child/subclass) to inherit attributes and methods from another class (parent/superclass). It promotes code reuse and creates hierarchical relationships between classes.

---

### 2. What does `super()` do?

**Your answer:**


**Correct answer:** `super()` calls methods from the parent class. It's commonly used in `__init__` to initialize the parent class, or to extend parent methods while keeping their functionality.

---

### 3. Can a class inherit from multiple parent classes?

**Your answer:**


**Correct answer:** Yes, Python supports multiple inheritance. A class can inherit from multiple parents: `class Child(Parent1, Parent2)`. Method resolution follows the MRO (Method Resolution Order).

---

### 4. What is an abstract base class (ABC)?

**Your answer:**


**Correct answer:** An ABC defines a template for other classes. It contains abstract methods (using `@abstractmethod`) that must be implemented by subclasses. You cannot instantiate an ABC directly.

---

### 5. When should you use inheritance vs composition?

**Your answer:**


**Correct answer:** Use inheritance for "is-a" relationships (Dog is-a Animal). Use composition for "has-a" relationships (Car has-a Engine). Composition is often more flexible and preferred for complex systems.

---

## Score Yourself
- 5/5: Excellent! - 3-4/5: Good! - 0-2/5: Review

## Next Steps
- Move to Day 14: List Comprehensions
