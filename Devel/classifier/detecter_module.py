import json
import xml.etree.ElementTree as ET
import re
import yaml
import pandas as pd
import os
import io
from PIL import Image

class FileFormatDetector:
    def __init__(self, file_path):
        self.file_path = file_path

    def detect_format(self):
        _, file_extension = os.path.splitext(self.file_path)
        with open(self.file_path, 'rb') as file:  # Open in binary mode for non-text files
            content = file.read()

        file_format = None
        if self.is_json(content):
            file_format = "JSON"
        elif self.is_xml(content):
            file_format = "XML"        
        elif self.is_yaml(content):
            file_format = "YAML"
        elif self.is_csv(content):
            file_format = "CSV"
        elif self.is_excel(content):
            file_format = "Excel"
        elif self.is_image(content):
            file_format = "non-text"
        else:
            file_format = "txt"

        return file_format, (file_format.lower() == file_extension[1:].lower())

    def is_image(self, content):
        try:
            img = Image.open(io.BytesIO(content))
            img.verify()  # Verify that it's a valid image
            return True
        except:
            return False

    def is_json(self, content):
        try:
            json.loads(content)
            return True
        except ValueError:
            return False

    def is_excel(self, content):
        try:
            pd.read_excel(io.BytesIO(content))  # Read from a binary stream
            return True
        except:
            return False

    def is_yaml(self, content):
        try:
            yaml.safe_load(content)
            # Additional check for distinctive YAML features like colons, indentation
            if ':' in content and any(line.startswith(' ') for line in content.splitlines()):
                return True
            else:
                return False
        except yaml.YAMLError:
            return False

    def is_csv(self, content):
        # Improved CSV detection with stricter sniffing and delimiter detection
        try:
            dialect = csv.Sniffer().sniff(content, delimiters=[',', ';', '\t', '|'])
            # Additional check to ensure multiple rows and a common delimiter
            reader = csv.reader(io.StringIO(content), dialect)
            if len(list(reader)) > 1 and all(len(row) > 1 for row in reader):  # Ensure multiple rows and columns
                return True
            else:
                return False
        except csv.Error:
            return False

    def is_xml(self, content):
        # Enhanced XML detection using regex (for more robust detection)
        xml_regex = re.compile(b'<\?xml\s+version=[\'"]([^\'"]+)[\'"]\s+encoding=[\'"]([^\'"]+)[\'"]\s*\?>')
        if xml_regex.match(content):
            return True
        # Fallback to ElementTree for further validation
        try:
            ET.fromstring(content)
            return True
        except ET.ParseError:
            return False
