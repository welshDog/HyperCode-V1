#!/usr/bin/env python3
"""
MCP Servers Startup Script

This script starts all available MCP servers.
Usage: python start_servers.py [server_name]
If server_name is provided, only that server will be started.
"""

import sys
import subprocess
import importlib
from pathlib import Path

# Add parent directory to Python path to allow importing mcp
sys.path.insert(0, str(Path(__file__).parent.parent))

# List of available servers
SERVERS = [
    "valkey_service",
    "dataset_downloader",
    "user_profile_manager",
    "aws_resource_manager",
    "path_service",
    "file_system",
    "code_analysis",
    "web_search",
    "human_input",
    "aws_cli",
    "hypercode_syntax",
]


def start_server(server_name):
    """Start a specific MCP server"""
    try:
        print(f"Starting {server_name}...")

        # Import the module to check if it exists
        module = importlib.import_module(f"mcp.servers.{server_name}")

        # Check if the module has a main function
        if hasattr(module, "main"):
            # Run the module as a script from the parent directory
            parent_dir = Path(__file__).parent.parent
            subprocess.run(
                [sys.executable, "-m", f"mcp.servers.{server_name}"],
                cwd=str(parent_dir),
            )
        else:
            print(f"Warning: {server_name} does not have a main() function")

    except ImportError as e:
        print(f"Error: Could not import {server_name}: {e}")
    except Exception as e:
        print(f"Error starting {server_name}: {e}")


def list_servers():
    """List all available servers"""
    print("Available MCP servers:")
    for i, server in enumerate(SERVERS, 1):
        print(f"  {i}. {server}")


def main():
    if len(sys.argv) > 1:
        server_name = sys.argv[1]
        if server_name in ["--help", "-h"]:
            print("Usage: python start_servers.py [server_name]")
            print("If server_name is provided, only that server will be started.")
            print("Available servers:")
            for server in SERVERS:
                print(f"  - {server}")
            return

        if server_name == "--list":
            list_servers()
            return

        if server_name not in SERVERS:
            print(f"Error: Unknown server '{server_name}'")
            list_servers()
            return

        start_server(server_name)
    else:
        print("Starting all MCP servers...")
        print(
            "Note: Some servers may fail to start if required services (like Redis) are not running."
        )
        print()

        for server in SERVERS:
            print(f"\n{'='*50}")
            start_server(server)
            print()


if __name__ == "__main__":
    main()
