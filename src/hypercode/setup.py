# setup.py
from setuptools import find_packages, setup

setup(
    name="hypercode",
    version="0.1.0",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8",
    install_requires=[],
    extras_require={
        "dev": [
            "pytest>=7.2.0",
            "pytest-cov>=4.0.0",
            "mypy>=0.991",
            "black>=22.12.0",
            "isort>=5.12.0",
            "flake8>=6.0.0",
        ]
    },
    entry_points={
        "console_scripts": [
            "hypercode-cli=hypercode.cli:cli",
        ],
    },
    # Include package data files
    include_package_data=True,
    # Add project URLs
    project_urls={
        "Source": "https://github.com/welshDog/hypercode",
        "Bug Tracker": "https://github.com/welshDog/hypercode/issues",
    },
    # Add classifiers
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    # Add long description
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
)
