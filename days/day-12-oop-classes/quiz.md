# Day 12 Quiz: Object-Oriented Programming

## Questions

### 1. What is the purpose of `__init__` method?

**Your answer:**


**Correct answer:** `__init__` is the constructor method that initializes a new object. It's called automatically when you create an instance and sets up the initial state (attributes) of the object.

---

### 2. What's the difference between instance and class variables?

**Your answer:**


**Correct answer:** Instance variables (defined in `__init__` with `self`) are unique to each object. Class variables (defined at class level) are shared by all instances of the class.

---

### 3. What does `self` represent?

**Your answer:**


**Correct answer:** `self` refers to the current instance of the class. It's used to access instance variables and methods. It must be the first parameter of instance methods.

---

### 4. When would you use a @property decorator?

**Your answer:**


**Correct answer:** Use `@property` to create computed attributes or add validation/logic when getting or setting attributes. It makes methods accessible like attributes (without parentheses).

---

### 5. What's the difference between @classmethod and @staticmethod?

**Your answer:**


**Correct answer:** `@classmethod` receives the class as first argument (cls) and can access/modify class state. `@staticmethod` doesn't receive class or instance, it's just a regular function grouped with the class for organization.

---

## Score Yourself
- 5/5: Excellent! - 3-4/5: Good! - 0-2/5: Review

## Next Steps
- Move to Day 13: OOP - Inheritance
