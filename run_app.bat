@echo off
echo ========================================
echo   Extrovert & Introvert Predictor
echo   Launching Streamlit App
echo ========================================
echo.

:: Check if virtual environment exists
if not exist "venv" (
    echo ERROR: Virtual environment not found!
    echo Please run setup_env.bat first to create the environment.
    echo.
    pause
    exit /b 1
)

:: Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo ERROR: Failed to activate virtual environment
    pause
    exit /b 1
)

echo Virtual environment activated!
echo.

:: Check if streamlit app exists
if not exist "streamlit_app.py" (
    echo ERROR: streamlit_app.py not found!
    echo Please ensure you're in the correct directory.
    pause
    exit /b 1
)

:: Check if data directory exists
if not exist "Data" (
    echo WARNING: Data directory not found!
    echo The app may not work properly without the training data.
    echo.
)

echo Starting Streamlit app...
echo The app will open in your default web browser.
echo To stop the app, press Ctrl+C in this window.
echo.
echo ========================================

:: Run the streamlit app using the virtual environment streamlit
venv\Scripts\streamlit.exe run streamlit_app.py

echo.
echo App stopped.
pause 