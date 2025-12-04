"""
Day 23: Virtual Environments and pip - Solutions
"""

import os
import subprocess
import sys

print("="*60)
print("Day 23: Virtual Environments and pip")
print("="*60)
print()

# Exercise 1
print("Exercise 1: Understanding Virtual Environments")
print("""
Virtual environments isolate project dependencies:
- Each project has its own packages
- Avoid version conflicts
- Easy to reproduce environments
- Clean system Python installation

Creating a virtual environment:
  python -m venv myenv

Activating:
  Mac/Linux: source myenv/bin/activate
  Windows: myenv\\Scripts\\activate

Deactivating:
  deactivate
""")

# Exercise 2
print("Exercise 2: Managing Packages")
print("""
Install packages:
  pip install pandas
  pip install numpy requests matplotlib

List installed:
  pip list

Show package info:
  pip show pandas

Uninstall:
  pip uninstall package_name
""")

# Exercise 3
print("Exercise 3: Requirements File")
print("""
Create requirements.txt:
  pip freeze > requirements.txt

Example requirements.txt:
  pandas==2.0.3
  numpy==1.24.3
  requests==2.31.0

Install from requirements:
  pip install -r requirements.txt

This ensures everyone has the same package versions!
""")

# Exercise 4
print("Exercise 4: Package Versions")
print("""
Specific version:
  pip install pandas==2.0.0

Minimum version:
  pip install "pandas>=2.0"

Version range:
  pip install "numpy>=1.20,<2.0"

Latest version:
  pip install --upgrade pandas
""")

# Exercise 5
print("Exercise 5: Project Setup Script")

def setup_project(project_name):
    """Create project structure with virtual environment"""
    print(f"\nSetting up project: {project_name}")
    
    # Create project directory
    if not os.path.exists(project_name):
        os.makedirs(project_name)
        print(f"✓ Created directory: {project_name}")
    
    # Create subdirectories
    subdirs = ["src", "tests", "data", "docs"]
    for subdir in subdirs:
        path = os.path.join(project_name, subdir)
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"✓ Created: {subdir}/")
    
    # Create files
    files = {
        "README.md": f"# {project_name}\n\nProject description here.\n",
        "requirements.txt": "# Add your dependencies here\n",
        ".gitignore": "venv/\n__pycache__/\n*.pyc\n.env\n",
        "src/__init__.py": "",
        "tests/__init__.py": ""
    }
    
    for filename, content in files.items():
        filepath = os.path.join(project_name, filename)
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, "w") as f:
            f.write(content)
        print(f"✓ Created: {filename}")
    
    print(f"\n✓ Project {project_name} setup complete!")
    print(f"\nNext steps:")
    print(f"  cd {project_name}")
    print(f"  python -m venv venv")
    print(f"  source venv/bin/activate")
    print(f"  pip install -r requirements.txt")

# Demo
setup_project("my_data_project")

# Cleanup
import shutil
if os.path.exists("my_data_project"):
    shutil.rmtree("my_data_project")

print("\n" + "="*60)
print("BONUS: Modern Alternatives")
print("="*60)
print("""
While pip + venv is the standard (and what you should master first),
be aware of modern alternatives:

1. uv (2024) - Extremely fast pip replacement
   - 10-100x faster than pip
   - Drop-in replacement: uv pip install pandas
   - Install: curl -LsSf https://astral.sh/uv/install.sh | sh
   - Best for: Speed, CI/CD pipelines

2. Poetry - Dependency management + packaging
   - Better dependency resolution
   - Lock files for reproducibility
   - Built-in project management
   - Best for: Complex projects, library development

3. Conda - Data science ecosystem
   - Handles non-Python dependencies
   - Popular in data science
   - Anaconda ecosystem
   - Best for: Data science, Jupyter notebooks

Recommendation:
- ✅ Master pip + venv first (universal, standard)
- ✅ Explore uv for speed once comfortable
- ✅ Try poetry for complex projects
- ✅ Use conda if working heavily in data science

For this course, stick with pip + venv!
""")

print("\n" + "="*60)
print("Day 23 Complete! Move to Day 24")
print("="*60)
