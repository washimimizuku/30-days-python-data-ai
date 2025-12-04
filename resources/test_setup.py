"""
Setup verification script for 30 Days of Python
Run this to verify your environment is ready
"""

import sys

def check_python_version():
    """Check Python version is 3.11+"""
    version = sys.version_info
    if version.major == 3 and version.minor >= 11:
        print(f"✅ Python version: {version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print(f"❌ Python version: {version.major}.{version.minor}.{version.micro}")
        print("   Please install Python 3.11 or higher")
        return False

def check_package(package_name):
    """Check if a package is installed"""
    try:
        __import__(package_name)
        print(f"✅ {package_name} installed")
        return True
    except ImportError:
        print(f"❌ {package_name} not installed")
        print(f"   Run: pip install {package_name}")
        return False

def main():
    """Run all checks"""
    print("Checking Python setup for 30 Days of Python...\n")
    
    # Core packages (required)
    print("Core Packages (Required):")
    core_checks = [
        check_python_version(),
        check_package("numpy"),
        check_package("pandas"),
        check_package("matplotlib"),
        check_package("requests"),
    ]
    
    # Optional packages
    print("\nOptional Packages (Install when needed):")
    optional_checks = [
        check_package("pydantic"),
        check_package("pytest"),
        check_package("jupyter"),
    ]
    
    print("\n" + "="*50)
    if all(core_checks):
        print("✅ All core packages installed! Ready to start Day 1")
        if not all(optional_checks):
            print("ℹ️  Some optional packages missing - install them when you reach those days")
        print("="*50)
        return 0
    else:
        print("❌ Some core packages missing. Please install:")
        print("   pip install numpy pandas matplotlib requests")
        print("="*50)
        return 1

if __name__ == "__main__":
    sys.exit(main())
