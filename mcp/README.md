# HyperCode MCP Servers

This directory contains Model Context Protocol (MCP) servers for the HyperCode framework.

## Available Servers

1. **valkey_service** - Redis/Valkey database service with FastAPI endpoints
2. **dataset_downloader** - Dataset downloading and management
3. **user_profile_manager** - User profile management
4. **aws_resource_manager** - AWS resource management
5. **path_service** - File path utilities
6. **file_system** - File system operations
7. **code_analysis** - Code analysis tools
8. **web_search** - Web search capabilities
9. **human_input** - Human input interfaces
10. **aws_cli** - AWS CLI integration
11. **hypercode_syntax** - HyperCode syntax processing

## Installation

1. Install required dependencies:
```bash
pip install -r requirements.txt
```

2. Ensure the HyperCode src directory is in your Python path (this should be automatic if you're working from the main hypercode directory).

## Usage

### Start All Servers
```bash
python start_servers.py
```

### Start a Specific Server
```bash
python start_servers.py path_service
```

### List Available Servers
```bash
python start_servers.py --list
```

### Start Servers Individually
You can also start servers directly using Python's module system:
```bash
cd ..  # Go to the hypercode root directory
python -m mcp.servers.valkey_service
python -m mcp.servers.path_service
```

## Configuration

The MCP servers are configured via the `config/mcp.json` file in the main hypercode directory. This file defines which servers are available and how they should be started.

## Server Details

### Valkey Service
- **Port**: 8001
- **Dependencies**: Redis/Valkey server running on localhost:6379
- **Endpoints**: 
  - `GET /` - Health check
  - `POST /set/{key}` - Set key-value pair
  - `GET /get/{key}` - Get value by key
  - `POST /hset/{name}/{key}` - Set field in hash
  - `GET /hget/{name}/{key}` - Get field from hash
  - `GET /hgetall/{name}` - Get all hash fields

### Other Servers
Most other servers are currently stub implementations that print a startup message. They can be extended with full functionality as needed.

## Development

To add a new server:

1. Create a new Python file in `mcp/servers/`
2. Implement a `main()` function that starts your server
3. Add the server name to the `SERVERS` list in `start_servers.py`
4. Add the import to `mcp/servers/__init__.py`
5. Update the configuration in `config/mcp.json` if needed

## Troubleshooting

### Module Import Errors
If you get "No module named 'mcp.servers'" errors:
1. Make sure you're running from the correct directory
2. Ensure the hypercode src directory is in your Python path
3. Try running from the main hypercode directory instead of the mcp subdirectory

### Redis Connection Errors
The valkey_service requires Redis/Valkey to be running. You can:
1. Install and start Redis locally
2. Use Docker: `docker run -d -p 6379:6379 redis`
3. Modify the REDIS_HOST and REDIS_PORT environment variables

### Port Conflicts
If you get port conflict errors, modify the SERVER_PORT variable in the respective server file.
