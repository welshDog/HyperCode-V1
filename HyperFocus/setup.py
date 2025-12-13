from setuptools import find_packages, setup  # type: ignore

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="hyperfocus",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A hyperfocus productivity tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/hyperfocus",
    packages=find_packages(include=["hyperfocus", "hyperfocus.*"]),
    package_data={
        "hyperfocus": ["*.yaml"],
    },
    include_package_data=True,
    install_requires=[
        "rich>=10.0.0",
        "pydantic>=1.8.0",
        "pyyaml>=6.0",
        "typer>=0.4.0",
        "sqlalchemy>=2.0.0",
        "alembic>=1.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "black>=21.0",
            "isort>=5.0.0",
            "mypy>=0.900",
        ],
    },
    entry_points={
        "console_scripts": [
            "hyperfocus=hyperfocus.__main__:app",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
