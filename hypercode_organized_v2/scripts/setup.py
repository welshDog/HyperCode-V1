# setup.py
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="hypercode",
    version="0.1.0",
    packages=find_packages(include=['hypercode', 'hypercode.*']),
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
    include_package_data=True,
    url="https://github.com/welshDog/hypercode",
    project_urls={
        "Source": "https://github.com/welshDog/hypercode",
        "Bug Tracker": "https://github.com/welshDog/hypercode/issues",
    },
    license="MIT",
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
    long_description=long_description,
    long_description_content_type="text/markdown",
)
