# Quick Start Guide - 30 Days of Python for Data and AI

Get started in 5 minutes! 🚀

> **📝 Note for macOS users:** Use `python3` instead of `python` throughout this guide. Your shell likely has `python` aliased to system Python, but `python3` will correctly use the virtual environment.

## Prerequisites

- Computer (Windows, Mac, or Linux)
- 5GB free disk space
- Internet connection

---

## Step 1: Install Python (5 minutes)

### Check if Python is already installed:
```bash
python --version
```

If you see `Python 3.11` or higher, skip to Step 2!

### Install Python:

**Windows:**
1. Download from [python.org/downloads](https://www.python.org/downloads/)
2. Run installer
3. ✅ **Check "Add Python to PATH"**
4. Click "Install Now"

**Mac:**
```bash
brew install python@3.11
```

**Linux:**
```bash
sudo apt update && sudo apt install python3.11 python3-pip
```

---

## Step 2: Download This Repository (1 minute)

**Option A: Download ZIP**
1. Click green "Code" button on GitHub
2. Select "Download ZIP"
3. Extract to your preferred location

**Option B: Clone with Git**
```bash
git clone https://github.com/YOUR-USERNAME/30-days-python-data-ai.git
cd 30-days-python-data-ai
```

---

## Step 3: Create Virtual Environment (1 minute)

Open terminal/command prompt in the project folder:

```bash
# Create virtual environment
# On Mac/Linux:
python3 -m venv venv

# On Windows:
python -m venv venv

# Activate it
# On Mac/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

You should see `(venv)` in your terminal prompt.

**Verify it's working (Mac/Linux):**
```bash
which python3  # Should show: .../venv/bin/python3 ✓
# Note: 'python' might still show system Python due to shell aliases
# That's OK - just use 'python3' for everything
```

---

## Step 4: Install Required Packages (2 minutes)

With the virtual environment activated:

```bash
# Mac/Linux - use python3 or pip:
python3 -m pip install -r requirements.txt
# OR just:
pip install -r requirements.txt

# Windows:
pip install -r requirements.txt

# For core packages only:
pip install numpy pandas matplotlib requests
```

---

## Step 5: Verify Setup (1 minute)

With virtual environment still activated:

```bash
python resources/test_setup.py
```

You should see:
```
✅ Python version: 3.11.x
✅ numpy installed
✅ pandas installed
✅ matplotlib installed
✅ requests installed
✅ All core packages installed! Ready to start Day 1
```

---

## Step 6: Start Learning! 🎉

Open the first lesson:
```bash
# Navigate to Day 1
cd days/day-01-variables-and-data-types

# Open README.md in your editor or browser
```

Or just open `days/day-01-variables-and-data-types/README.md` in any text editor!

---

## Daily Routine

**Before starting each day:**
```bash
# Make sure virtual environment is activated
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

**Then follow this pattern:**

1. **📖 Read** the `README.md` (15 min)
   - Learn the concepts
   - Study the code examples

2. **💻 Code** the `exercise.py` (40 min)
   - Complete the TODO exercises
   - Try before looking at solutions

3. **✅ Check** the `solution.py` (if stuck)
   - Compare your approach
   - Learn from the examples

4. **🎯 Quiz** with `quiz.md` (5 min)
   - Test your understanding
   - Review if needed

**When done for the day:**
```bash
deactivate  # Exit virtual environment
```

---

## Recommended Tools

### Code Editor (Choose One):

**VS Code** (Recommended for beginners)
- Download: [code.visualstudio.com](https://code.visualstudio.com/)
- Install Python extension
- Free and beginner-friendly

**PyCharm Community**
- Download: [jetbrains.com/pycharm](https://www.jetbrains.com/pycharm/)
- Full-featured Python IDE
- Free community edition

**Or use any text editor** + terminal!

---

## Learning Tips

✅ **Code along** - Type examples yourself, don't copy-paste  
✅ **Take breaks** - It's okay to split a day across sessions  
✅ **Practice more** - Try variations of exercises  
✅ **Ask questions** - Use community resources  
✅ **Be patient** - Learning takes time!

---

## Project Days (Extra Time Needed)

These days are mini-projects and may take 1.5-2 hours:
- **Day 10**: Data File Processor
- **Day 20**: Data Analysis Tool
- **Day 30**: ETL Pipeline (Capstone)

Don't rush these - they're where you consolidate your learning!

---

## Troubleshooting

### "Python not found"
- Restart terminal after installation
- Try `python3` instead of `python`
- Check PATH environment variable

### Virtual environment not activating
- Make sure you're in the project folder
- Try `python3 -m venv venv` instead
- On Windows, you may need to run: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

### macOS: "externally-managed-environment" error
Even with venv activated, you might see this error.

**Why:** Your shell has `python` aliased to system Python, but `python3` points to venv.

**Check:**
```bash
which python   # Shows: /opt/homebrew/bin/python3 (system)
which python3  # Shows: .../venv/bin/python3 (venv) ✓
```

**Solution: Use `python3` instead of `python`**
```bash
# Install packages with python3
python3 -m pip install -r requirements.txt

# Run scripts with python3
python3 resources/test_setup.py

# Or use pip directly (it's in venv)
pip install -r requirements.txt
```

### "pip not found"
```bash
python -m pip install --upgrade pip
```

### Package installation fails
```bash
# Make sure virtual environment is activated first!
pip install --upgrade pip setuptools wheel
pip install numpy pandas matplotlib requests
```

### Forgot to activate virtual environment?
```bash
# You'll see packages not found errors
# Solution: Activate it!
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### Still stuck?
1. Check [TROUBLESHOOTING.md](./TROUBLESHOOTING.md) for detailed solutions
2. Check [resources/SETUP.md](./resources/SETUP.md) for detailed instructions
3. Google the error message
4. Ask in community forums

---

## What's Next?

After completing all 30 days, you'll be ready for:
- 100 Days of Data and AI bootcamp
- Python-based data engineering projects
- Building ETL pipelines
- Working with APIs
- Further learning in web frameworks

---

## Need More Help?

- 📖 **Detailed Setup**: See [resources/SETUP.md](./resources/SETUP.md)
- 📝 **Quick Reference**: See [resources/cheatsheet.md](./resources/cheatsheet.md)
- 📚 **Curriculum Overview**: See [CURRICULUM.md](./CURRICULUM.md)
- 🏠 **Main README**: See [README.md](./README.md)

---

**Ready? Let's start with Day 1!** 🚀

Open `days/day-01-variables-and-data-types/README.md` and begin your journey!
