# Setup Guide - 30 Days of Python for Data and AI

## Prerequisites

- Computer with Windows, macOS, or Linux
- 5GB free disk space
- Internet connection

## Step 1: Install Python

### Windows
1. Download Python 3.11+ from [python.org](https://www.python.org/downloads/)
2. Run installer
3. ✅ Check "Add Python to PATH"
4. Click "Install Now"

### macOS
```bash
# Using Homebrew (recommended)
brew install python@3.11

# Or download from python.org
```

### Linux
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3.11 python3-pip

# Fedora
sudo dnf install python3.11
```

### Verify Installation
```bash
python --version  # Should show 3.11+
pip --version
```

## Step 2: Install VS Code (Recommended)

1. Download from [code.visualstudio.com](https://code.visualstudio.com/)
2. Install Python extension
3. Install Jupyter extension

### Alternative IDEs
- PyCharm Community Edition
- Jupyter Lab
- Any text editor + terminal

## Step 3: Set Up Virtual Environment

**Why use a virtual environment?**
- Isolates project dependencies
- Avoids conflicts with other Python projects
- Makes it easy to reproduce your setup
- Best practice for Python development

```bash
# Navigate to bootcamp folder
cd 30-days-python-data-ai

# Create virtual environment
# macOS/Linux (use python3):
python3 -m venv venv

# Windows:
python -m venv venv

# Activate it
# macOS/Linux:
source venv/bin/activate

# Windows (Command Prompt):
venv\Scripts\activate

# Windows (PowerShell):
venv\Scripts\Activate.ps1

# You should see (venv) in your prompt

# Verify (macOS/Linux):
which python  # Should show: .../venv/bin/python
```

**Install packages:**
```bash
# Core packages (required)
pip install numpy pandas matplotlib requests

# OR install everything (including optional)
pip install -r requirements.txt
```

**Deactivate when done:**
```bash
deactivate
```

## Step 4: Verify Setup

**Make sure virtual environment is activated** (you should see `(venv)` in prompt):

```bash
# Run test script
python tools/test_setup.py
```

Should output:
```
✅ Python version: 3.11.x
✅ numpy installed
✅ pandas installed
✅ matplotlib installed
✅ requests installed
✅ All core packages installed! Ready to start Day 1
```

## Folder Structure

```
30-days-python-data-ai/
├── README.md              # Overview
├── requirements.txt       # Python packages
├── docs/
│   ├── SETUP.md          # This file
│   ├── CURRICULUM.md     # Day-by-day breakdown
│   └── ...
├── tools/
│   ├── cheatsheet.md     # Quick reference
│   └── test_setup.py     # Verification
│   └── test_setup.py     # Setup verification
├── data/
│   ├── raw/              # Original data files
│   └── processed/        # Processed data
└── days/
    ├── day-01-variables-and-data-types/
    │   ├── README.md     # Day's lesson
    │   ├── exercise.py   # Practice exercises
    │   ├── solution.py   # Solutions
    │   └── quiz.md       # Quiz questions
    ├── day-02-operators-and-expressions/
    └── ... (day-30-capstone-etl-pipeline)
```

## Daily Workflow

**Start each session:**
```bash
# Activate virtual environment
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

**Then:**
1. **Read** the lesson in `days/day-XX-.../README.md` (15 min)
2. **Code** the exercises in `exercise.py` (40 min)
3. **Check** `solution.py` if stuck (don't peek too early!)
4. **Quiz** yourself with `quiz.md` (5 min)

**End each session:**
```bash
deactivate  # Exit virtual environment
```

**Note**: Project days (10, 20, 30) may take 1.5-2 hours - that's normal!

## Troubleshooting

### Python not found
- Restart terminal after installation
- Try `python3` instead of `python`
- Check PATH environment variable

### Virtual environment won't activate
**Windows PowerShell:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**macOS/Linux:**
- Make sure you're in the project directory
- Use `python3` instead of `python`: `python3 -m venv venv`
- After activation, verify: `which python` should show `venv/bin/python`

**macOS with Homebrew Python:**
If you see "externally-managed-environment" error even with venv activated:
```bash
# Your shell might have a python alias
# Solution: Use python3 explicitly
deactivate
rm -rf venv
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
```

### pip not working
```bash
python -m pip install --upgrade pip
```

### Package installation fails
```bash
# Make sure virtual environment is activated!
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

### "Module not found" errors
- Check if virtual environment is activated (look for `(venv)` in prompt)
- If not activated, run: `source venv/bin/activate` (Mac/Linux) or `venv\Scripts\activate` (Windows)
- Reinstall packages if needed

### Starting fresh
```bash
# Deactivate if active
deactivate

# Remove old virtual environment
rm -rf venv  # Mac/Linux
rmdir /s venv  # Windows

# Create new one
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# Reinstall packages
pip install -r requirements.txt
```

## Getting Help

- Check `tools/cheatsheet.md` for quick reference
- Google error messages
- Ask in community Discord
- Review previous days if concepts are unclear

## Ready to Start?

Once setup is complete:
1. Open `days/day-01-variables-and-data-types/README.md`
2. Read the lesson
3. Complete the exercises
4. Have fun learning Python! 🚀
