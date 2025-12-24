#!/usr/bin/env python3
"""
Test script for HyperCode MCP Server integration
"""

import asyncio
import json
import sys
from pathlib import Path

# Add src to path for importing parser
sys.path.append(str(Path(__file__).parent / "src" / "parser"))


async def test_mcp_server():
    """Test the MCP server functionality"""

    # Import the MCP server
    sys.path.append(str(Path(__file__).parent / "mcp" / "servers"))
    from hypercode_syntax import HyperCodeSyntaxServer

    server = HyperCodeSyntaxServer()

    print("🧪 Testing HyperCode MCP Server Integration")
    print("=" * 50)

    # Test 1: Initialize
    print("\n1. Testing initialization...")
    init_request = {
        "method": "initialize",
        "params": {"clientInfo": {"name": "test-client", "version": "1.0.0"}},
    }

    response = await server.handle_request(init_request)
    print(f"✅ Initialize response: {json.dumps(response, indent=2)}")

    # Test 2: Document parsing
    print("\n2. Testing document parsing...")
    test_code = """🔍 @verifiable("formal_proof")
📐 @ensures("output.shape == (batch, classes)")
📋 @requires("input.shape[1] == features")
🧠 @intent("Classify input features")
🎯 @accessibility("high_contrast", "dyslexia_font")
function classifier(input: Tensor[batch, features]) -> Tensor[batch, classes] {
    🎨 weights = initialize(features, classes)
    ⚡ logits = matmul(input, weights)
    🔄 return softmax(logits)
}"""

    parse_request = {
        "method": "hypercode/parse",
        "params": {"uri": "test://example.hyper", "content": test_code},
    }

    # Simulate document change
    change_request = {
        "method": "textDocument/didChange",
        "params": {
            "textDocument": {"uri": "test://example.hyper"},
            "content": [{"text": test_code}],
        },
    }

    # First update the cache
    await server.handle_request(change_request)

    # Then parse
    response = await server.handle_request(parse_request)
    print(f"✅ Parse response: {json.dumps(response, indent=2)}")

    # Test 3: Neurodiversity validation
    print("\n3. Testing neurodiversity validation...")
    validate_request = {
        "method": "hypercode/validate",
        "params": {"uri": "test://example.hyper"},
    }

    response = await server.handle_request(validate_request)
    print(f"✅ Validation response: {json.dumps(response, indent=2)}")

    # Test 4: Hover functionality
    print("\n4. Testing hover functionality...")
    hover_request = {
        "method": "textDocument/hover",
        "params": {
            "textDocument": {"uri": "test://example.hyper"},
            "position": {"line": 0, "character": 5},
        },
    }

    response = await server.handle_request(hover_request)
    print(f"✅ Hover response: {json.dumps(response, indent=2)}")

    # Test 5: Completion
    print("\n5. Testing completion...")
    completion_request = {
        "method": "textDocument/completion",
        "params": {
            "textDocument": {"uri": "test://example.hyper"},
            "position": {"line": 10, "character": 0},
        },
    }

    response = await server.handle_request(completion_request)
    print(f"✅ Completion response: {json.dumps(response, indent=2)}")

    print("\n🎉 All MCP Server tests completed successfully!")


if __name__ == "__main__":
    asyncio.run(test_mcp_server())
