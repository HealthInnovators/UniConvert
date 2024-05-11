# CSV File Generator

## Overview
`generate_csv` is a Python function that scans a specified directory for files and generates a summary CSV report with metadata. The report includes details such as the file path, whether it's empty, if it has a wrong extension, the given and actual extensions, and whether it's faulty.

## Features
- Scans all files in a specified directory.
- Extracts and analyzes metadata like empty files, faulty files, and extension mismatches.
- Outputs a CSV report containing file metadata for review or further processing.

## Usage Example

To use the `generate_csv` function, pass the path of the directory containing your files as an argument.

```python
from csv_generator import generate_csv

# Replace 'your_directory_path' with the path to the directory containing your files
generate_csv('your_directory_path')
