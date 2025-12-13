# tools/install.py
#!/usr/bin/env python3

import os
import sys
import platform
import subprocess
import venv
from pathlib import Path

def check_python_version():
    """Check if Python 3.10+ is installed."""
    if sys.version_info < (3, 10):
        print("❌ Python 3.10 or higher is required.")
        print(f"Current Python version: {platform.python_version()}")
        sys.exit(1)

def create_virtualenv(venv_path=".venv"):
    """Create a Python virtual environment."""
    print("🔧 Creating virtual environment...")
    try:
        venv.create(venv_path, with_pip=True)
        return True
    except Exception as e:
        print(f"❌ Failed to create virtual environment: {e}")
        return False

def install_dependencies(venv_path=".venv"):
    """Install project dependencies."""
    print("📦 Installing dependencies...")
    pip = os.path.join(venv_path, "bin" if platform.system() != "Windows" else "Scripts", "pip")
    if platform.system() == "Windows":
        pip += ".exe"
    
    try:
        subprocess.run([pip, "install", "-e", ".[dev]"], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False

def main():
    print("🚀 Setting up HyperCode development environment...")
    print(f"Platform: {platform.system()} {platform.release()}")
    print(f"Python: {platform.python_version()}")
    
    # Check Python version
    check_python_version()
    
    # Create virtual environment
    if not create_virtualenv():
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        sys.exit(1)
    
    print("\n🎉 Setup completed successfully!")
    print("\nTo activate the virtual environment, run:")
    if platform.system() == "Windows":
        print("  .\\.venv\\Scripts\\activate")
    else:
        print("  source .venv/bin/activate")
    print("\nTo verify the installation, run:")
       print("  hypercode --version")

if __name__ == "__main__":""
    main()