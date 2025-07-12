@echo off
echo ========================================
echo   Extrovert & Introvert Predictor
echo   Environment Setup for Windows
echo ========================================
echo.

:: Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://python.org
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

echo Python found! Checking version...
python --version
echo.

:: Check if pip is available
pip --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: pip is not available
    echo Please ensure pip is installed with Python
    pause
    exit /b 1
)

echo pip found! Checking version...
pip --version
echo.

:: Create virtual environment
echo Creating virtual environment...
if exist "venv" (
    echo Virtual environment already exists. Removing old one...
    rmdir /s /q venv
)

python -m venv venv
if errorlevel 1 (
    echo ERROR: Failed to create virtual environment
    echo Please ensure you have the venv module installed
    pause
    exit /b 1
)

echo Virtual environment created successfully!
echo.

:: Activate virtual environment and use full paths
echo Activating virtual environment...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo ERROR: Failed to activate virtual environment
    pause
    exit /b 1
)

echo Virtual environment activated!
echo.

:: Use the full path to python and pip in the virtual environment
set PYTHON_PATH=venv\Scripts\python.exe
set PIP_PATH=venv\Scripts\pip.exe

:: Check if the virtual environment python exists
if not exist "%PYTHON_PATH%" (
    echo ERROR: Python not found in virtual environment
    echo Path checked: %PYTHON_PATH%
    pause
    exit /b 1
)

:: Upgrade pip using the virtual environment pip
echo Upgrading pip...
"%PYTHON_PATH%" -m pip install --upgrade pip
echo.

:: Install requirements using the virtual environment pip
echo Installing required packages...
if exist "requirements.txt" (
    "%PIP_PATH%" install -r requirements.txt
    if errorlevel 1 (
        echo ERROR: Failed to install requirements
        pause
        exit /b 1
    )
    echo.
    echo All packages installed successfully!
) else (
    echo WARNING: requirements.txt not found
    echo Installing basic packages manually...
    "%PIP_PATH%" install streamlit>=1.28.0 pandas>=1.5.0 numpy>=1.21.0 scikit-learn>=1.1.0
    if errorlevel 1 (
        echo ERROR: Failed to install packages
        pause
        exit /b 1
    )
    echo.
    echo Basic packages installed successfully!
)

echo.
echo ========================================
echo   Environment Setup Complete!
echo ========================================
echo.
echo To run the app:
echo 1. Activate the virtual environment: venv\Scripts\activate.bat
echo 2. Run the app: streamlit run streamlit_app.py
echo.
echo Or use the run_app.bat file for convenience.
echo.
echo Press any key to exit...
pause >nul 