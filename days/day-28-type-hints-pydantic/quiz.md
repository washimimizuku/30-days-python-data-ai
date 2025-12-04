# Day 28 Quiz: Type Hints and Pydantic

## Questions

### 1. What are type hints in Python?

**Your answer:**


**Correct answer:** Type hints are annotations that specify expected types for variables, function parameters, and return values. They improve code readability and enable static type checking with tools like mypy.

---

### 2. What does Optional[str] mean?

**Your answer:**


**Correct answer:** `Optional[str]` means the value can be either a string or None. It's equivalent to `Union[str, None]`. Use for optional parameters or nullable values.

---

### 3. What is Pydantic used for?

**Your answer:**


**Correct answer:** Pydantic provides data validation and settings management using Python type hints. It automatically validates data, converts types, and provides clear error messages.

---

### 4. How do you create a Pydantic model?

**Your answer:**


**Correct answer:** Inherit from `BaseModel` and define fields with type hints: `class User(BaseModel): name: str; age: int`. Pydantic handles validation automatically.

---

### 5. Why use type hints?

**Your answer:**


**Correct answer:** Type hints improve code documentation, enable IDE autocomplete, catch bugs early with static analysis, make refactoring safer, and serve as inline documentation.

---

## Score Yourself
- 5/5: Excellent! - 3-4/5: Good! - 0-2/5: Review

## Next Steps
- Move to Day 29: Testing with pytest
