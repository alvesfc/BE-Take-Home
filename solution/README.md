# Excel Spreadsheet Analyzer
This project analyzes dependencies in an Excel spreadsheet and calculates the values of cells based on their formulas 
and dependencies.

## Pre-requisites
- Python 3.6 or higher
- pip (Python package installer)

## Setup

1. Step 1: Create a Virtual Environment
```bash
python3 -m venv solution/.venv  # On Unix or MacOS

```

2. Step 2: Activate the Virtual Environment
```bash
source solution/.venv/bin/activate # On Unix or MacOS
```

3. Step 3: Install Required Packages
```bash
pip install -r solution/requirements.txt
```

## Usage

### Running the Program
To run the program, execute the main.py file:
```bash
python3 solution/src/main.py <path_to_excel_file> <sheet_name>
```
You can use the provided sample Excel file to test the program:
```bash
python3 solution/src/main.py 'solution/data/Financial_Projections.xlsx' 'Sheet1'
```

### Running the Tests
To run the tests, execute the test_excel_analyzer.py file:
```bash
python3 solution/tests/test_excel_analyzer.py
```


