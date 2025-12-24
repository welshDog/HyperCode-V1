@echo off
echo Cleaning HyperCode project...

:: Remove Python cache
del /s /q *.pyc
del /s /q *.pyo
del /s /q *.pyd
rmdir /s /q __pycache__

:: Remove build artifacts
rmdir /s /q build
rmdir /s /q dist
rmdir /s /q *.egg-info

:: Remove virtual environment
if exist .venv rmdir /s /q .venv

echo Clean complete!
