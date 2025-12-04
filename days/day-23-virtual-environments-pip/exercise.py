"""
Day 23: Virtual Environments and pip - Exercises
"""

# Exercise 1: Understanding Virtual Environments
# TODO: Learn about venv and why it's important
# Commands to run in terminal (not in Python):
# python -m venv myenv
# source myenv/bin/activate  # On Mac/Linux
# myenv\Scripts\activate  # On Windows

# Exercise 2: Managing Packages
# TODO: Install packages with pip
# pip install pandas numpy requests

# TODO: List installed packages
# pip list

# TODO: Show package info
# pip show pandas

# Exercise 3: Requirements File
# TODO: Create requirements.txt
# pip freeze > requirements.txt

# TODO: Install from requirements
# pip install -r requirements.txt

# Exercise 4: Package Versions
# TODO: Install specific versions
# pip install pandas==2.0.0
# pip install "numpy>=1.20,<2.0"

# Exercise 5: Project Setup Script
# TODO: Create a setup script for a new project

def setup_project(project_name):
    """
    Create project structure with virtual environment
    """
    # TODO: Implement project setup
    pass

if __name__ == "__main__":
    print("Day 23: Virtual Environments")
    print("\nKey Commands:")
    print("  python -m venv venv")
    print("  source venv/bin/activate")
    print("  pip install package_name")
    print("  pip freeze > requirements.txt")
    print("  deactivate")
