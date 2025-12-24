@echo off
echo Setting up HyperCode development environment...

:: Create virtual environment
python -m venv .venv
call .venv\Scripts\activate

:: Install dependencies
pip install --upgrade pip
pip install -r config\requirements.txt
pip install -r config\requirements-dev.txt

:: Install pre-commit hooks
pre-commit install

echo Setup complete! Activate the virtual environment with: .venv\Scripts\activate
