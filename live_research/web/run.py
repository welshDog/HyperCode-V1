#!/usr/bin/env python3
"""
Run the research web application.
"""

import os
from app import app

if __name__ == "__main__":
    # Create necessary directories
    os.makedirs("static", exist_ok=True)
    os.makedirs("templates", exist_ok=True)

    # Run the app
    app.run(debug=True, port=5000)
