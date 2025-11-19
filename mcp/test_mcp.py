#!/usr/bin/env python3
"""
MCP Servers Test Script

This script tests that all MCP servers can be imported and have the expected structure.
"""

import sys
from pathlib import Path

# Add parent directory to Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

def test_server_imports():
    """Test that all servers can be imported"""
    servers = [
        'valkey_service',
        'dataset_downloader', 
        'user_profile_manager',
        'aws_resource_manager',
        'path_service',
        'file_system',
        'code_analysis',
        'web_search',
        'human_input',
        'aws_cli',
        'hypercode_syntax'
    ]
    
    results = {}
    
    for server_name in servers:
        try:
            module = __import__(f'mcp.servers.{server_name}', fromlist=[server_name])
            results[server_name] = {
                'imported': True,
                'has_main': hasattr(module, 'main'),
                'module': module
            }
        except Exception as e:
            results[server_name] = {
                'imported': False,
                'error': str(e)
            }
    
    return results

def main():
    print("Testing MCP Servers...")
    print("=" * 50)
    
    results = test_server_imports()
    
    imported_count = 0
    main_count = 0
    
    for server_name, result in results.items():
        status = "OK" if result['imported'] else "FAIL"
        print(f"{status} {server_name}")
        
        if result['imported']:
            imported_count += 1
            if result.get('has_main'):
                main_count += 1
                print(f"    - Has main() function")
            else:
                print(f"    - No main() function")
        else:
            print(f"    - Error: {result.get('error', 'Unknown error')}")
    
    print("=" * 50)
    print(f"Results: {imported_count}/{len(results)} servers imported successfully")
    print(f"         {main_count}/{len(results)} servers have main() function")
    
    if imported_count == len(results):
        print("All servers imported successfully!")
        return 0
    else:
        print("Some servers failed to import")
        return 1

if __name__ == "__main__":
    sys.exit(main())
