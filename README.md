# Digit Recognizer

A simple digit recognition project using Python, TensorFlow, and Tkinter. This tool allows users to draw a digit in a window, which the trained model then predicts.

## Project Structure

- **`DrawingInterface.py`**: Creates a Tkinter window where users can draw a digit. Based on the drawing, the trained model predicts the digit.
- **`training.py`**: Trains the digit recognition model using a dataset of digits stored in CSV files (`train.csv` and `test.csv`). This script creates and saves a model that can be used for predictions.
- **`main.py`**: Runs the Tkinter app (calls `DrawingInterface.py`) to interact with the trained model.

## How to Run the Project

1. **Train the Model** (Optional if you already have a trained model -> ./models/handwritten.keras):
   ```bash
   python training.py
    ```
2. **Run the Digit Recognizer App:**
    ```bash
    python main.py
    ```

## Requirements
- Python 3.x
- TensorFlow
- Tkinter
- Pillow
- Numpy
- Keras
- Keras-Utils
- Pandas
- Scikit-learn
- Install dependencies using:
```
pip install -r requirements.txt
```

## Enabling Long Path Support

Some Python packages may generate long file paths, especially on Windows. If you encounter any issues, follow these steps to enable long path support:

### Enabling Long Paths with PowerShell

1. Open PowerShell as Administrator.
2. Run the following command:
    ```powershell
    Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name "LongPathsEnabled" -Value 1
    ```

### Enabling Long Paths with Command Prompt (CMD)

1. Open Command Prompt as Administrator.
2. Run the following command:
    ```cmd
    reg add "HKLM\SYSTEM\CurrentControlSet\Control\FileSystem" /v LongPathsEnabled /t REG_DWORD /d 1 /f
    ```
After enabling this setting, you may need to restart your system for changes to take effect.