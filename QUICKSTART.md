# Quick Start Guide - 30 Days of Python for Data and AI

Get started in 5 minutes! 🚀

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

## Step 3: Install Required Packages (2 minutes)

Open terminal/command prompt in the project folder:

```bash
# Install core packages (required)
pip install numpy pandas matplotlib requests

# OR install everything (including optional)
pip install -r requirements.txt
```

---

## Step 4: Verify Setup (1 minute)

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

## Step 5: Start Learning! 🎉

Open the first lesson:
```bash
# Navigate to Day 1
cd days/day-01-variables-and-data-types

# Open README.md in your editor or browser
```

Or just open `days/day-01-variables-and-data-types/README.md` in any text editor!

---

## Daily Routine

Each day, follow this pattern:

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

### "pip not found"
```bash
python -m pip install --upgrade pip
```

### Package installation fails
```bash
pip install --upgrade pip setuptools wheel
pip install numpy pandas matplotlib requests
```

### Still stuck?
1. Check [resources/SETUP.md](./resources/SETUP.md) for detailed instructions
2. Google the error message
3. Ask in community forums

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
