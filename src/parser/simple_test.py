#!/usr/bin/env python3
import re

# Test the pattern directly
pattern = re.compile(r"🔍\s*@verifiable\s*\((.*?)\)")

test_line = '🔍 @verifiable("formal_proof")'
matches = pattern.findall(test_line)

print(f"Test line: {test_line}")
print(f"Matches: {matches}")
print(f"Pattern works: {len(matches) > 0}")
