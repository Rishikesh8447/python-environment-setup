# Python Environment Setup Automation

A simple Python automation script that prepares the basic structure of a Python project automatically.

Instead of manually creating folders and configuration files, the setup script performs the initial project configuration with a single command.

## Features

- Checks the installed Python version
- Validates that Python 3.8 or higher is installed
- Creates standard project directories
- Generates `requirements.txt`
- Generates `.gitignore`
- Handles filesystem errors using exception handling
- Displays colored terminal output
- Uses modular functions for better code organization

## Project Structure

```text
python-environment-setup/
│
├── setup.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── src/
├── tests/
├── docs/
└── logs/
```

## Technologies Used

- Python
- pathlib
- sys
- Exception Handling
- Git / GitHub

## How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Navigate to the project

```bash
cd python-environment-setup
```

### 3. Run the setup script

```bash
python setup.py
```

## What the Script Does

The script follows this workflow:

```text
Run setup.py
     ↓
Check Python version
     ↓
Create project directories
     ↓
Create requirements.txt
     ↓
Create .gitignore
     ↓
Setup completed
```

## Concepts Practiced

This project was created to practice and understand:

- Variables
- Functions
- Conditional statements
- Loops
- f-strings
- Modules
- `sys.version_info`
- `pathlib`
- File handling
- Exception handling
- Git and `.gitignore`
- Basic project automation

## Purpose

The main purpose of this project is to demonstrate how Python can be used to automate repetitive development tasks and create a standardized project structure.

## Future Improvements

Possible improvements include:

- Automatically creating a virtual environment
- Installing dependencies automatically
- Adding logging
- Adding automated tests
- Supporting command-line arguments
- Adding more project templates