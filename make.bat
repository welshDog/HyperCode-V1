@echo off

if "%1"=="benchmark" goto benchmark
if "%1"=="clean" goto clean
if "%1"=="test" goto test
if "%1"=="help" goto help

:benchmark
echo Running HyperCode Benchmarks...
python core\src\ci_pipeline.py
goto end

:test
echo Running Tests...
# Assuming standard pytest discovery
python -m pytest
goto end

:clean
echo Cleaning up...
del /S *.pyc
rmdir /S /Q __pycache__
goto end

:help
echo Available commands:
echo   make benchmark  - Run performance benchmarks
echo   make test       - Run unit tests
echo   make clean      - Clean temporary files
goto end

:end
