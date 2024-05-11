# FileConverter

## Overview
`FileConverter` is a Python class designed to convert files between various data formats, including XML, YAML, CSV, JSON, and Excel. It employs robust data reading and writing methods using `pandas`, `xmltodict`, and `yaml` to enable seamless conversion between supported formats.

## Features
- Converts files between XML, YAML, CSV, JSON, and Excel formats.
- Validates input file paths, formats, and checks permissions.
- Offers flexibility to add custom reader and writer functions.
- Error handling and logging for data import/export issues.

## Usage Example

Below is an example demonstrating how to convert a YAML file to a JSON file using `FileConverter`.

```python
from file_converter import FileConverter

# Set input and output file paths and their respective formats
input_file_path = "input.yaml"
output_file_path = "output.json"

# Initialize the FileConverter object
converter = FileConverter(input_file_path, "yaml", output_file_path, "json")

# Perform the conversion
result = converter.convert_file()
print(result)
