from setuptools import find_packages, setup

setup(
    name="hypercode",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "hypercode=hypercode.__main__:main",
        ],
    },
    python_requires=">=3.8",
)
