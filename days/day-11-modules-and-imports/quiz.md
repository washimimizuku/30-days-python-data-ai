# Day 11 Quiz: Modules and Imports

## Questions

### 1. What's the difference between `import math` and `from math import sqrt`?

**Your answer:**


**Correct answer:** `import math` imports the entire module (use as `math.sqrt()`), while `from math import sqrt` imports only the sqrt function (use as `sqrt()`). The second uses less namespace but can cause naming conflicts.

---

### 2. What is `__init__.py` used for?

**Your answer:**


**Correct answer:** It marks a directory as a Python package, allowing imports from that directory. It can also contain initialization code that runs when the package is imported. In Python 3.3+, it's optional but still commonly used.

---

### 3. Why use import aliases (e.g., `import pandas as pd`)?

**Your answer:**


**Correct answer:** Aliases make code shorter and more readable, especially for commonly used libraries with long names. They're also conventional in the community (pd for pandas, np for numpy).

---

### 4. What does `if __name__ == "__main__":` do?

**Your answer:**


**Correct answer:** It checks if the script is being run directly (not imported). Code inside this block only executes when the file is run as the main program, not when imported as a module.

---

### 5. How do you see what's available in a module?

**Your answer:**


**Correct answer:** Use `dir(module_name)` to list all attributes and functions, or `help(module_name)` for detailed documentation. You can also check the module's `__doc__` attribute.

---

## Score Yourself
- 5/5: Excellent! - 3-4/5: Good! - 0-2/5: Review

## Next Steps
- Move to Day 12: Object-Oriented Programming
