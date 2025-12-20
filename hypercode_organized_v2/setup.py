from setuptools import setup, find_packages

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
            "black>=22.0.0",
            "isort>=5.10.0",
            "mypy>=0.910",
            "flake8>=4.0.0",
            "pre-commit>=2.17.0",
            "lark-parser>=0.11.0",
            "sphinx>=5.0.0",
            "sphinx-rtd-theme>=1.0.0",
        ]
    }
)
