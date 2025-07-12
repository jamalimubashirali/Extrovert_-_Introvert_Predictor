# Windows Setup Guide for Extrovert & Introvert Predictor

This guide will help you set up and run the Personality Predictor app on Windows.

## Prerequisites

1. **Python**: Make sure Python is installed on your system
   - Download from [python.org](https://python.org)
   - During installation, make sure to check "Add Python to PATH"
   - Recommended version: Python 3.8 or higher

2. **Windows PowerShell or Command Prompt**: The batch files work with both

## Quick Setup

### Option 1: Automated Setup (Recommended)

1. **Double-click** `setup_env.bat` to automatically:
   - Check if Python is installed
   - Create a virtual environment
   - Install all required packages
   - Set up everything needed to run the app

2. **Double-click** `run_app.bat` to launch the app

### Option 2: Manual Setup

If you prefer to set up manually:

1. Open Command Prompt or PowerShell in the project directory
2. Create virtual environment: `python -m venv venv`
3. Activate it: `venv\Scripts\activate.bat`
4. Install requirements: `pip install -r requirements.txt`
5. Run the app: `streamlit run streamlit_app.py`

## What the Batch Files Do

### `setup_env.bat`
- ✅ Checks if Python is installed and accessible
- ✅ Verifies pip is available
- ✅ Creates a fresh virtual environment (`venv`)
- ✅ Activates the virtual environment
- ✅ Upgrades pip to the latest version
- ✅ Installs all required packages from `requirements.txt`
- ✅ Provides clear error messages if anything goes wrong

### `run_app.bat`
- ✅ Checks if the virtual environment exists
- ✅ Activates the virtual environment
- ✅ Verifies the app file exists
- ✅ Checks for the data directory
- ✅ Launches the Streamlit app
- ✅ Opens the app in your default web browser

## Troubleshooting

### "Python is not recognized"
- Make sure Python is installed and added to PATH
- Try restarting your command prompt after installing Python

### "Virtual environment activation failed"
- Make sure you're running the batch file from the project directory
- Try running as administrator if needed

### "Requirements installation failed"
- Check your internet connection
- Try running `pip install --upgrade pip` first
- Some packages might need Microsoft Visual C++ Build Tools

### "Streamlit app not found"
- Make sure `streamlit_app.py` is in the same directory as the batch files

### "Data directory not found"
- The app needs the `Data/` folder with training data
- Make sure the `Data/` directory exists and contains `train.csv`

## Running the App

After setup, you can run the app in two ways:

1. **Double-click** `run_app.bat` (easiest)
2. **Manual method**:
   ```cmd
   venv\Scripts\activate.bat
   streamlit run streamlit_app.py
   ```

The app will open in your default web browser at `http://localhost:8501`

## Stopping the App

- Press `Ctrl+C` in the command prompt window where the app is running
- Or simply close the command prompt window

## File Structure

After setup, your directory should look like this:
```
Extrovert_&_Introvert_Predictor/
├── setup_env.bat          # Environment setup script
├── run_app.bat           # App launcher script
├── streamlit_app.py      # Main application
├── requirements.txt      # Python dependencies
├── Data/                # Training data directory
├── venv/               # Virtual environment (created by setup)
└── WINDOWS_SETUP.md    # This file
```

## Notes

- The virtual environment (`venv`) is created locally and won't affect your system Python
- You can delete the `venv` folder anytime and run `setup_env.bat` again to recreate it
- The app uses machine learning to predict personality traits based on user input
- All dependencies are specified in `requirements.txt` and will be installed automatically 