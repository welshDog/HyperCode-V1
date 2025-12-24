from pathlib import Path

import pytest


@pytest.fixture
def sample_code():
    return """
    print 'Hello, World!'
    let x = 10
    if x > 5 {
        print 'x is greater than 5'
    }
    """
