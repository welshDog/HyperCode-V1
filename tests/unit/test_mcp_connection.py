import json
import socket
import subprocess
from typing import Any, Dict, List, Optional, Tuple

import requests

# List of MCP servers from the README
MCP_SERVERS = [
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

# Common ports to check
COMMON_PORTS = [8000, 8080, 5000, 3000, 9000]


def check_port(host: str, port: int, timeout: float = 1.0) -> bool:
    """Check if a port is open on the given host."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            return s.connect_ex((host, port)) == 0
    except Exception:
        return False


def find_running_servers(host: str = "localhost") -> List[Tuple[str, int]]:
    """Scan common ports to find running servers."""
    print("\nScanning for running servers on common ports...")
    running_servers = []

    for port in COMMON_PORTS:
        if check_port(host, port):
            running_servers.append(("http", host, port))
            print(f"✅ Found server running on {host}:{port}")

    return running_servers


def test_server_connection(
    server_name: str, base_url: str = None, port: int = None
) -> Dict[str, Any]:
    """Test connection to a single MCP server."""
    endpoints = ["/health", "/", f"/{server_name}/health", f"/{server_name}"]

    # Try different URL patterns
    if base_url:
        urls_to_try = [
            f"{base_url.rstrip('/')}/{server_name}{endpoint}" for endpoint in endpoints
        ]
        urls_to_try.append(base_url)  # Also try the base URL directly
    else:
        # If no base URL, try with and without the server name in the path
        urls_to_try = []
        for port in [port] if port else COMMON_PORTS:
            urls_to_try.extend(
                [f"http://localhost:{port}{endpoint}" for endpoint in endpoints]
            )

    for url in urls_to_try:
        try:
            response = requests.get(url, timeout=2)
            if response.status_code < 500:  # Accept any non-5xx status code
                return {
                    "status": "success",
                    "server": server_name,
                    "url": url,
                    "status_code": response.status_code,
                    "response": response.json() if response.content else "No content",
                }
        except (requests.RequestException, json.JSONDecodeError):
            continue

    return {
        "status": "error",
        "server": server_name,
        "error": f"Could not connect to any known endpoints",
    }


def test_all_servers():
    """Test connection to all MCP servers and print results."""
    print("Testing connections to MCP servers...\n")

    # First, try to find any running servers
    running_servers = find_running_servers()

    if not running_servers:
        print(
            "\n❌ No running servers detected on common ports. Please ensure the MCP servers are running."
        )
        print("\nTo start the MCP servers, you might need to run a command like:")
        print("  python -m mcp.servers  # or check the project's documentation")
        return []

    print("\nTesting each MCP service...\n")

    results = []
    for server in MCP_SERVERS:
        print(f"Testing {server}...")

        # Try each running server
        for protocol, host, port in running_servers:
            base_url = f"{protocol}://{host}:{port}"
            result = test_server_connection(server, base_url, port)
            if result["status"] == "success":
                break
        else:
            # If no success with any server, try without base URL
            result = test_server_connection(server)

        results.append(result)

        # Print status with color coding
        if result["status"] == "success":
            print(
                f"✅ {server}: Connected successfully at {result.get('url', 'unknown')}"
            )
            if "response" in result and result["response"] != "No content":
                print(f"   Response: {json.dumps(result['response'], indent=2)}")
        else:
            print(
                f"❌ {server}: {result.get('error', 'Could not connect to any known endpoints')}"
            )
        print("-" * 50)

    return results


def check_dependencies():
    """Check if required dependencies are installed."""
    try:
        import requests

        return True
    except ImportError:
        print("\n❌ The 'requests' package is required but not installed.")
        print("Install it with: pip install requests")
        return False


if __name__ == "__main__":
    if check_dependencies():
        test_all_servers()

        print("\nTroubleshooting Tips:")
        print("1. Make sure the MCP servers are running")
        print("2. Check if the servers are running on non-standard ports")
        print("3. Verify that the server URLs match the expected format")
        print("4. Check if there are any firewall rules blocking the connections")
        print("\nFor more help, check the project's documentation or README file.")
