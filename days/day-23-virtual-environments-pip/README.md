# Day 23: Virtual Environments and pip

## 📖 Learning Objectives (15 min)

- Understand why virtual environments are essential
- Create and manage virtual environments with venv
- Install and manage packages with pip
- Use requirements.txt for reproducible environments
- Learn about modern package management alternatives

---

## Theory

### Why Virtual Environments?

Virtual environments isolate project dependencies:
- Each project has its own packages
- Avoid version conflicts between projects
- Easy to reproduce environments
- Keep system Python clean

**Example Problem Without Virtual Environments:**
```
Project A needs pandas==1.5.0
Project B needs pandas==2.0.0
❌ Conflict! Only one can be installed globally
```

**Solution: Virtual Environments**
```
Project A: venv_a/ → pandas==1.5.0
Project B: venv_b/ → pandas==2.0.0
✅ Both work independently!
```

### Creating Virtual Environments

```bash
# Create virtual environment
python -m venv myenv

# Activate (Mac/Linux)
source myenv/bin/activate

# Activate (Windows)
myenv\Scripts\activate

# Your prompt changes to show active environment
(myenv) $

# Deactivate
deactivate
```

### Managing Packages with pip

```bash
# Install a package
pip install pandas

# Install specific version
pip install pandas==2.0.3

# Install multiple packages
pip install pandas numpy matplotlib

# Upgrade a package
pip install --upgrade pandas

# Uninstall
pip uninstall pandas

# List installed packages
pip list

# Show package details
pip show pandas
```

### Requirements Files

**Create requirements.txt:**
```bash
# Save all installed packages
pip freeze > requirements.txt
```

**Example requirements.txt:**
```
pandas==2.0.3
numpy==1.24.3
requests==2.31.0
matplotlib==3.7.1
```

**Install from requirements.txt:**
```bash
pip install -r requirements.txt
```

### Version Specifiers

```bash
# Exact version
pip install pandas==2.0.0

# Minimum version
pip install "pandas>=2.0"

# Version range
pip install "numpy>=1.20,<2.0"

# Compatible release (patch updates only)
pip install "requests~=2.31.0"  # Allows 2.31.x
```

### Best Practices

1. **Always use virtual environments** - Never install packages globally
2. **Pin versions in requirements.txt** - Ensures reproducibility
3. **Keep requirements.txt updated** - Run `pip freeze` after changes
4. **Use .gitignore** - Don't commit venv/ folder to git
5. **Document setup** - Add setup instructions to README

---

## Modern Alternatives

While pip + venv is the standard and what you should learn first, be aware of modern alternatives:

### uv (2024 - Recommended for Advanced Users)
```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create project with uv (much faster than pip)
uv venv
uv pip install pandas numpy

# Why uv?
# - 10-100x faster than pip
# - Drop-in replacement for pip
# - Written in Rust
# - Growing adoption
```

**When to use:** When you need speed, especially with large projects or CI/CD pipelines.

### Poetry
```bash
# Install poetry
curl -sSL https://install.python-poetry.org | python3 -

# Create new project
poetry new myproject
poetry add pandas numpy

# Why Poetry?
# - Better dependency resolution
# - Lock files (poetry.lock)
# - Built-in project management
# - Handles virtual environments automatically
```

**When to use:** Complex projects with many dependencies, library development, when you need strict dependency management.

### Conda
```bash
# Create environment
conda create -n myenv python=3.11
conda activate myenv
conda install pandas numpy

# Why Conda?
# - Popular in data science
# - Handles non-Python dependencies (C libraries)
# - Anaconda ecosystem
```

**When to use:** Data science projects, when you need non-Python dependencies, working with Jupyter notebooks.

### Comparison Table

| Tool | Speed | Ease of Use | Best For |
|------|-------|-------------|----------|
| **pip + venv** | Medium | ⭐⭐⭐⭐⭐ Easy | Learning, standard projects |
| **uv** | ⚡ Very Fast | ⭐⭐⭐⭐ Easy | Speed-critical, CI/CD |
| **poetry** | Medium | ⭐⭐⭐ Moderate | Complex dependencies, libraries |
| **conda** | Slow | ⭐⭐⭐ Moderate | Data science, non-Python deps |

### Our Recommendation

**For this course and beginners:**
- ✅ Start with **pip + venv** (standard, universal, simple)
- ✅ Master the fundamentals first
- ✅ Explore alternatives once comfortable

**As you advance:**
- Consider **uv** for faster installs
- Use **poetry** for library development
- Try **conda** if working heavily in data science

---

## 💻 Exercises (40 min)

Complete `exercise.py`

### Exercise 1: Create Virtual Environment
Create a virtual environment for a data project

### Exercise 2: Install Packages
Install pandas, numpy, and matplotlib

### Exercise 3: Requirements File
Create and use requirements.txt

### Exercise 4: Version Management
Practice installing specific versions

### Exercise 5: Project Setup
Set up a complete project structure with virtual environment

---

## ✅ Quiz (5 min)

See `quiz.md`

---

## 🎯 Key Takeaways

- Virtual environments isolate project dependencies
- pip is the standard Python package manager
- requirements.txt ensures reproducible environments
- Always activate your virtual environment before installing packages
- Modern alternatives exist (uv, poetry, conda) but learn pip first

---

## 📚 Additional Resources

- [Python venv documentation](https://docs.python.org/3/library/venv.html)
- [pip documentation](https://pip.pypa.io/)
- [uv documentation](https://github.com/astral-sh/uv)
- [Poetry documentation](https://python-poetry.org/)

---

## Tomorrow: Day 24 - Jupyter Notebooks
