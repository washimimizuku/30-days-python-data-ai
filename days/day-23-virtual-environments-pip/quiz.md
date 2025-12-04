# Day 23 Quiz: Virtual Environments and pip

## Questions

### 1. Why use virtual environments?

**Your answer:**


**Correct answer:** Virtual environments isolate project dependencies, preventing version conflicts between projects. Each project can have its own package versions without affecting the system Python or other projects.

---

### 2. How do you create a virtual environment?

**Your answer:**


**Correct answer:** Use `python -m venv venv` (or any name instead of "venv"). This creates a new directory with an isolated Python environment.

---

### 3. What does `pip freeze` do?

**Your answer:**


**Correct answer:** `pip freeze` lists all installed packages and their exact versions in a format suitable for requirements.txt. Use `pip freeze > requirements.txt` to save dependencies.

---

### 4. How do you install packages from requirements.txt?

**Your answer:**


**Correct answer:** Use `pip install -r requirements.txt`. This installs all packages listed in the file with their specified versions.

---

### 5. What's the difference between `pip install pandas` and `pip install pandas==2.0.0`?

**Your answer:**


**Correct answer:** Without version, pip installs the latest version. With `==2.0.0`, it installs that specific version. Use specific versions for reproducibility.

---

### 6. BONUS: When might you consider using alternatives to pip?

**Your answer:**


**Correct answer:** Consider alternatives when: you need faster installs (uv), complex dependency management (poetry), or working heavily in data science with non-Python dependencies (conda). However, master pip + venv first as it's the universal standard.

---

## Score Yourself
- 6/6: Excellent! You understand package management deeply
- 5/6: Great! You know the essentials
- 3-4/6: Good! Review the concepts you missed
- 0-2/6: Review today's lesson and try exercises again

## Key Takeaway

**Start with pip + venv** - it's the standard, works everywhere, and is what most tutorials and documentation assume. Once comfortable, explore modern alternatives based on your specific needs.

## Next Steps
- Move to Day 24: Jupyter Notebooks
