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

```bash
# Navigate to bootcamp folder
cd 30-days-python-data-ai

# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install required packages
pip install -r requirements.txt
```

## Step 4: Verify Setup

```bash
# Run test script
python resources/test_setup.py
```

Should output:
```
✅ Python version: 3.11.x
✅ NumPy installed
✅ Pandas installed
✅ Matplotlib installed
✅ All set! Ready to start Day 1
```

## Folder Structure

```
30-days-python-data-ai/
├── README.md              # Overview
├── CURRICULUM.md          # Day-by-day breakdown
├── requirements.txt       # Python packages
├── resources/
│   ├── SETUP.md          # This file
│   ├── cheatsheet.md     # Quick reference
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

1. **Read** the lesson in `days/day-XX-.../README.md` (15 min)
2. **Code** the exercises in `exercise.py` (40 min)
3. **Check** `solution.py` if stuck (don't peek too early!)
4. **Quiz** yourself with `quiz.md` (5 min)

**Note**: Project days (10, 20, 30) may take 1.5-2 hours - that's normal!

## Troubleshooting

### Python not found
- Restart terminal after installation
- Check PATH environment variable

### pip not working
```bash
python -m pip install --upgrade pip
```

### Virtual environment issues
- Delete `venv` folder and recreate
- Use `python3` instead of `python` on some systems

### Package installation fails
```bash
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

## Getting Help

- Check `resources/cheatsheet.md` for quick reference
- Google error messages
- Ask in community Discord
- Review previous days if concepts are unclear

## Ready to Start?

Once setup is complete:
1. Open `days/day-01-variables-and-data-types/README.md`
2. Read the lesson
3. Complete the exercises
4. Have fun learning Python! 🚀
