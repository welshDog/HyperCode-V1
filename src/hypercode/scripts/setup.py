# setup.py
from setuptools import find_packages, setup

setup(
    name="hypercode",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=[],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=22.1.0",
            "flake8>=4.0.0",
            "mypy>=0.930",
            "pytest-cov>=3.0.0",
        ],
    },
)
