# Personality Predictor: Extrovert vs Introvert

A Streamlit web application that predicts whether a person is more of an Extrovert or Introvert based on their behavioral characteristics and social preferences.

## Features

- **Interactive Interface**: User-friendly form to input personal characteristics
- **Machine Learning Model**: Uses Logistic Regression trained on 18,526 samples
- **Real-time Prediction**: Instant personality prediction with confidence scores
- **Detailed Insights**: Provides characteristics and traits for each personality type
- **Beautiful UI**: Modern, responsive design with gradient cards and emojis

## Features Used for Prediction

The model analyzes the following characteristics:

### Time & Social Behavior
- **Hours spent alone per day**: How much time you spend in solitude
- **Social events attended per month**: Frequency of social gatherings
- **Times going outside per week**: How often you leave your home
- **Number of close friends**: Size of your social circle
- **Social media posts per week**: Online social activity

### Psychological Traits
- **Stage fear**: Whether you experience anxiety in public speaking
- **Drained after socializing**: Whether social interactions exhaust you

## Quick Start (Recommended)

### Windows Users
1. **Double-click** `setup_environment.bat` to create and set up the virtual environment
2. **Double-click** `run_app.bat` to start the Streamlit app

### Mac/Linux Users
1. **Make scripts executable and run setup:**
   ```bash
   chmod +x setup_environment.sh run_app.sh
   ./setup_environment.sh
   ```
2. **Run the app:**
   ```bash
   ./run_app.sh
   ```

## Manual Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Step-by-Step Setup

1. **Create a virtual environment** (recommended):
   ```bash
   # Windows
   python -m venv personality_env
   
   # Mac/Linux
   python3 -m venv personality_env
   ```

2. **Activate the virtual environment**:
   ```bash
   # Windows
   personality_env\Scripts\activate.bat
   
   # Mac/Linux
   source personality_env/bin/activate
   ```

3. **Upgrade pip**:
   ```bash
   python -m pip install --upgrade pip
   ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Ensure the data file is in the correct location**:
   - Make sure `Data/train.csv` exists in the project directory

## Running the Application

### Option 1: Using the provided scripts (Recommended)
- **Windows**: Double-click `run_app.bat`
- **Mac/Linux**: Run `./run_app.sh`

### Option 2: Manual activation and run
1. **Activate the virtual environment**:
   ```bash
   # Windows
   personality_env\Scripts\activate.bat
   
   # Mac/Linux
   source personality_env/bin/activate
   ```

2. **Start the Streamlit app**:
   ```bash
   streamlit run streamlit_app.py
   ```

3. **Open your browser**:
   - The app will automatically open at `http://localhost:8501`
   - If it doesn't open automatically, manually navigate to the URL

## How to Use

1. **Enter Your Characteristics**: Use the sliders and dropdown menus to input your behavioral patterns
2. **Click Predict**: Press the "🔮 Predict My Personality" button
3. **View Results**: See your predicted personality type with confidence scores
4. **Read Insights**: Learn about the characteristics of your predicted personality type

## Model Information

- **Algorithm**: Logistic Regression
- **Training Data**: 18,526 samples
- **Accuracy**: ~85% (varies based on cross-validation)
- **Features**: 7 behavioral and psychological characteristics

## Technical Details

- **Framework**: Streamlit
- **Machine Learning**: Scikit-learn
- **Data Processing**: Pandas, NumPy
- **Model**: Logistic Regression with feature preprocessing
- **Environment**: Virtual environment for dependency isolation

## Virtual Environment Benefits

Using a virtual environment provides several advantages:
- **Isolation**: Prevents conflicts between project dependencies
- **Reproducibility**: Ensures consistent environment across different machines
- **Clean Installation**: Keeps your system Python installation clean
- **Easy Management**: Simple to create, activate, and delete environments

## Important Notes

- **Personality Spectrum**: Remember that personality exists on a spectrum
- **Behavioral Patterns**: The prediction is based on behavioral patterns, not definitive labels
- **Honest Input**: For best results, be honest about your typical behaviors and preferences
- **General Guide**: Use this as a general guide rather than a definitive personality assessment

## File Structure

```
├── streamlit_app.py          # Main Streamlit application
├── predict_the_introverts_from_the_extroverts.py  # Original model training script
├── requirements.txt          # Python dependencies
├── setup_environment.bat     # Windows environment setup script
├── run_app.bat              # Windows app launcher
├── setup_environment.sh      # Unix/Linux/Mac environment setup script
├── run_app.sh               # Unix/Linux/Mac app launcher
├── README.md               # This file
└── Data/
    └── train.csv           # Training dataset
```

## Troubleshooting

- **Data not found**: Ensure `Data/train.csv` exists in the project directory
- **Dependencies error**: Make sure you're in the virtual environment and run `pip install -r requirements.txt`
- **Port already in use**: Streamlit will automatically use the next available port
- **Virtual environment not found**: Run the setup script again or manually create the environment
- **Permission denied (Mac/Linux)**: Make scripts executable with `chmod +x *.sh`

## Environment Management

### Activating the Environment
```bash
# Windows
personality_env\Scripts\activate.bat

# Mac/Linux
source personality_env/bin/activate
```

### Deactivating the Environment
```bash
deactivate
```

### Deleting the Environment (if needed)
```bash
# Windows
rmdir /s personality_env

# Mac/Linux
rm -rf personality_env
```

## Contributing

Feel free to improve the app by:
- Adding more features to the prediction model
- Enhancing the UI/UX
- Adding data visualization
- Improving the model accuracy 