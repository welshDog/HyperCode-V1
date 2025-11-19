#!/usr/bin/env python3
"""
MCP Setup Script

This script helps set up the MCP environment by:
1. Installing dependencies
2. Verifying the setup
3. Providing guidance for next steps
"""

import subprocess
import sys
from pathlib import Path

def install_dependencies():
    """Install required dependencies"""
    print("Installing MCP dependencies...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], 
                      check=True)
        print("Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to install dependencies: {e}")
        return False

def verify_setup():
    """Verify that MCP is properly set up"""
    print("\nVerifying MCP setup...")
    try:
        result = subprocess.run([sys.executable, "test_mcp.py"], 
                              capture_output=True, text=True, cwd=Path(__file__).parent)
        if result.returncode == 0:
            print("MCP setup verification passed")
            return True
        else:
            print("MCP setup verification failed")
            print(result.stdout)
            print(result.stderr)
            return False
    except Exception as e:
        print(f"Error during verification: {e}")
        return False

def show_next_steps():
    """Show next steps for using MCP"""
    print("\n" + "="*50)
    print("MCP Setup Complete!")
    print("="*50)
    print("\nNext steps:")
    print("1. Start servers:")
    print("   python start_servers.py --list")
    print("   python start_servers.py path_service")
    print("\n2. Or start all servers:")
    print("   python start_servers.py")
    print("\n3. For Redis-dependent services (like valkey_service):")
    print("   - Install Redis locally or use Docker:")
    print("   docker run -d -p 6379:6379 redis")
    print("\n4. Check the README.md for detailed documentation")
    print("\n5. Configuration is in: ../config/mcp.json")

def main():
    print("HyperCode MCP Setup")
    print("="*30)
    
    # Check if we're in the right directory
    if not Path("requirements.txt").exists():
        print("Error: Please run this script from the mcp directory")
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        sys.exit(1)
    
    # Verify setup
    if not verify_setup():
        print("\nSetup verification failed, but dependencies were installed.")
        print("You may need to check your Python path or environment.")
    
    # Show next steps
    show_next_steps()

if __name__ == "__main__":
    main()
