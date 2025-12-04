# Day 29 Quiz: Testing with pytest

## Questions

### 1. Why write tests?

**Your answer:**


**Correct answer:** Tests catch bugs early, document expected behavior, enable safe refactoring, provide confidence in code changes, and serve as executable documentation.

---

### 2. What is a test fixture?

**Your answer:**


**Correct answer:** A fixture is reusable test data or setup code. Use `@pytest.fixture` decorator to create fixtures that can be injected into test functions as parameters.

---

### 3. What does assert do in tests?

**Your answer:**


**Correct answer:** `assert` checks if a condition is True. If False, the test fails. Example: `assert result == expected`. pytest provides detailed failure messages.

---

### 4. How do you run pytest?

**Your answer:**


**Correct answer:** Run `pytest` in terminal to discover and run all test files (test_*.py or *_test.py). Use `pytest -v` for verbose output, `pytest test_file.py` for specific file.

---

### 5. What is test coverage?

**Your answer:**


**Correct answer:** Coverage measures what percentage of code is executed by tests. Use `pytest --cov=module` to check coverage. Aim for high coverage but focus on testing important logic.

---

## Score Yourself
- 5/5: Excellent! - 3-4/5: Good! - 0-2/5: Review

## Next Steps
- Move to Day 30: Capstone ETL Pipeline Project!
