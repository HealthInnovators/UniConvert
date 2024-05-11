# test_classifier_module.py
import os
import io
import pytest
from PIL import Image
import json
import pandas as pd
import csv
import re
import xml.etree.ElementTree as ET
import yaml
from detecter_module import FileFormatDetector

# Test cases for FileFormatDetector class
class TestFileFormatDetector:
    def test_detect_format_json(self):
        file_path = os.path.join(os.getcwd(), 'test_data', 'sample.json')  
        detector = FileFormatDetector(file_path)
        expected_format = "JSON"
        result, is_extension_match = detector.detect_format()
        assert result == expected_format
        assert is_extension_match is True
  
    def test_detect_format_xml(self):
        file_path = os.path.join(os.getcwd(), '', 'test_data/sample.xml')
        # Add other test cases for different file formats
        detector = FileFormatDetector(file_path) 
        expected_format = "XML"      
        result, is_extension_match = detector.detect_format()
        assert result == expected_format
        assert is_extension_match is TrueIt 

    # rest of the test cases for csv, excel, yaml, and image.
   .....

   def test_is_xml(self):
        valid_xml_content = b'<?xml version="1.0" encoding="UTF-8"?><root></root>'
        assert FileFormatDetector.is_xml(valid_xml_content) is True
        invalid_xml_content = b'<invalid_xml>'
        assert FileFormatDetector.is_xml(invalid_xml_content) is False
  
    # Similar tests for is_json, is_csv, is_excel, and is_yaml functions
    .....