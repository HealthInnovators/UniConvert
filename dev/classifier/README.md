# File Format Detector

## Overview
This Python script, `FileFormatDetector`, is designed to identify the format of a given file based on its content and extension. It supports a wide range of file types including JSON, XML, YAML, CSV, Excel, and various image formats. The script employs various libraries such as `json`, `xml.etree.ElementTree`, `re`, `yaml`, `pandas`, and `PIL` to perform the detection.

## Features
- Supports detection of multiple file formats: JSON, XML, YAML, CSV, Excel, images, and plain text.
- Validates if the content matches the file's extension.
- Utilizes robust methods for file type validation, including content sniffing and binary checks.

## Usage Example

To use the `FileFormatDetector`, you need to instantiate the class with the path of the file you want to check, and then call the `detect_format()` method to get the file format and whether the format matches the extension.

```python
from file_format_detector import FileFormatDetector

# Create an instance with the path to the file you want to check
detector = FileFormatDetector('path/to/your/file.extension')

# Detect the file format
format_detected, is_match = detector.detect_format()

print(f"Detected Format: {format_detected}")
print(f"Format matches extension: {is_match}")
