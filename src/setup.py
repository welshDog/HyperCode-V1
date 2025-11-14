from setuptools import setup, find_packages

setup(
    name="hypercode",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'hypercode=hypercode.__main__:main',
        ],
    },
    python_requires='>=3.8',
)