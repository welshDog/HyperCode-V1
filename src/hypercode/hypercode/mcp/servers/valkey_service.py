# mcp/servers/valkey_service.py

import json
import os

import uvicorn
from fastapi import FastAPI, HTTPException
from redis import ConnectionError as RedisConnectionError
from redis import Redis

# --- Configuration ---
REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")
REDIS_PORT = int(os.environ.get("REDIS_PORT", 6379))
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 8001

# --- FastAPI Application ---
app = FastAPI(
    title="Valkey Service",
    description="A simple MCP server to interact with a Valkey/Redis data store.",
    version="1.0.0",
)

# --- Redis Connection ---
try:
    # The decode_responses=True argument ensures that we get strings from Redis, not bytes.
    redis_client = Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
    # Check the connection
    redis_client.ping()
    print(f"Successfully connected to Redis at {REDIS_HOST}:{REDIS_PORT}")
except RedisConnectionError as e:
    print(
        f"Error: Could not connect to Redis at {REDIS_HOST}:{REDIS_PORT}. Please ensure it is running."
    )
    print(f"Details: {e}")
    # We don't exit here, to allow for the server to start and report the error via HTTP
    redis_client = None


# --- Middleware for Connection Check ---
@app.middleware("http")
async def check_redis_connection(request, call_next):
    if redis_client is None:
        return HTTPException(
            status_code=503, detail="Service Unavailable: Could not connect to Redis."
        )
    try:
        redis_client.ping()
    except RedisConnectionError:
        return HTTPException(
            status_code=503, detail="Service Unavailable: Lost connection to Redis."
        )
    response = await call_next(request)
    return response


# --- API Endpoints ---


@app.get("/", summary="Health Check")
async def health_check():
    """
    Health check endpoint to verify that the service is running.
    """
    return {"status": "ok", "message": "Valkey Service is running."}


@app.post("/set/{key}", summary="Set a key-value pair")
async def set_key(key: str, value: dict):
    """
    Set a value for a given key. The value should be a JSON object.
    """
    try:
        # Redis can only store strings, so we serialize the JSON dict
        redis_client.set(key, json.dumps(value))
        return {"status": "ok", "key": key, "value": value}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/get/{key}", summary="Get a value by key")
async def get_key(key: str):
    """
    Get the value for a given key.
    """
    try:
        value_str = redis_client.get(key)
        if value_str is None:
            raise HTTPException(status_code=404, detail="Key not found")
        # Deserialize the JSON string back into a dict
        return {"status": "ok", "key": key, "value": json.loads(value_str)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/hset/{name}/{key}", summary="Set a field in a hash")
async def hset_key(name: str, key: str, value: dict):
    """
    Set a field (key) in a hash (name). The value should be a JSON object.
    """
    try:
        redis_client.hset(name, key, json.dumps(value))
        return {"status": "ok", "name": name, "key": key, "value": value}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/hget/{name}/{key}", summary="Get a field from a hash")
async def hget_key(name: str, key: str):
    """
    Get a field (key) from a hash (name).
    """
    try:
        value_str = redis_client.hget(name, key)
        if value_str is None:
            raise HTTPException(status_code=404, detail="Hash name or key not found")
        return {
            "status": "ok",
            "name": name,
            "key": key,
            "value": json.loads(value_str),
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/hgetall/{name}", summary="Get all fields and values from a hash")
async def hgetall_hash(name: str):
    """
    Get all fields and values for a given hash name.
    """
    try:
        all_values = redis_client.hgetall(name)
        if not all_values:
            raise HTTPException(status_code=404, detail="Hash not found")

        # Deserialize all values from JSON strings
        deserialized_values = {k: json.loads(v) for k, v in all_values.items()}

        return {"status": "ok", "name": name, "values": deserialized_values}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# --- Main entry point for running the server ---
def main():
    """

    Main function to run the Valkey Service MCP Server.
    This function is called when the script is executed directly.
    It starts the Uvicorn server, which in turn runs the FastAPI application.
    """
    print(f"Starting Valkey Service MCP Server on http://{SERVER_HOST}:{SERVER_PORT}")
    print("Press Ctrl+C to stop.")

    # Check if Redis is available before starting the server
    if redis_client is None:
        print(
            "\nFATAL: Could not connect to Redis. The server will not be able to serve requests."
        )
        print(
            "Please ensure Redis/Valkey is running and accessible at the configured host and port."
        )
        # We still run the server to provide HTTP error messages, but log a fatal warning.

    uvicorn.run(app, host=SERVER_HOST, port=SERVER_PORT)


if __name__ == "__main__":
    main()
