# Test Reorganization Script
# This script reorganizes the test files into a more structured layout

# Create necessary directories
$directories = @(
    "tests/unit/core",
    "tests/unit/ai",
    "tests/unit/utils",
    "tests/integration",
    "tests/performance"
)

foreach ($dir in $directories) {
    if (-not (Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir -Force
        Write-Host "Created directory: $dir"
    }
}

# Create __init__.py files
$initFiles = @(
    "tests/unit/__init__.py",
    "tests/unit/core/__init__.py",
    "tests/unit/ai/__init__.py",
    "tests/unit/utils/__init__.py",
    "tests/integration/__init__.py",
    "tests/performance/__init__.py"
)

foreach ($file in $initFiles) {
    if (-not (Test-Path $file)) {
        New-Item -ItemType File -Path $file -Force
        Write-Host "Created file: $file"
    }
}

# Move test files to appropriate locations
$testMappings = @{
    # Core functionality tests
    "test_lexer.py" = "tests/unit/core"
    "test_parser.py" = "tests/unit/core"
    "test_interpreter.py" = "tests/unit/core"
    "test_core.py" = "tests/unit/core"
    
    # AI integration tests
    "test_perplexity.py" = "tests/unit/ai"
    "test_perplexity_client.py" = "tests/unit/ai"
    "test_knowledge_base.py" = "tests/unit/ai"
    "test_mcp_integration.py" = "tests/unit/ai"
    
    # Utility tests
    "test_implementation_guide.py" = "tests/unit/utils"
    "test_direct_access.py" = "tests/unit/utils"
    
    # Integration tests
    "test_integration.py" = "tests/integration"
    "test_real_data.py" = "tests/integration"
    "test_real_space_data.py" = "tests/integration"
    "test_sensory_profiles.py" = "tests/integration"
    
    # Performance tests
    "benchmark_knowledge_base.py" = "tests/performance"
}

# Move the files
foreach ($file in $testMappings.Keys) {
    $source = "tests/$file"
    $destination = $testMappings[$file]
    
    if (Test-Path $source) {
        Move-Item -Path $source -Destination $destination -Force
        Write-Host "Moved $source to $destination"
    }
}

# Clean up empty test files
$emptyTestFiles = @(
    "test_interpreter_basics.py"
)

foreach ($file in $emptyTestFiles) {
    $path = "tests/$file"
    if (Test-Path $path) {
        Remove-Item $path
        Write-Host "Removed empty test file: $path"
    }
}

Write-Host "Test reorganization complete!"
