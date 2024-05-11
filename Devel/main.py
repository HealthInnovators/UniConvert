import os
import streamlit as st
from classifier.detecter_module import FileFormatDetector  # Import the FileFormatDetector class
from llm_converter.llm_converter import LLMConverter

converter = LLMConverter("llm_converter/schema.json")

# Create a header with the text "Welcome"
st.header("Welcome to UniConvert")

# Create an input box for the user to enter one to many files
files = st.file_uploader("Select file(s)", accept_multiple_files=True)

# Create a selectbox for the user to select the output type
output_type = st.selectbox("Select output type", ["JSON", "XML", "CSV", "YAML", "XLSX"])

# Create a button called submit
if st.button("Submit"):
    if not os.path.exists("temp"):
        os.makedirs("temp")

    # Detect the format of every entry file
    for file in files:
        content = file.getvalue().decode('utf-8')
        output = converter.convert(content)
        st.header("Original input:")
        st.text(content)
        st.header("Standard Output:")
        st.text(output)
    # Save the file to a temporary path
        # temp_path = os.path.join("temp", file.name)
        # with open(temp_path, 'wb') as f:
        #     print(str(file.getvalue()))
        #     exit()
            # f.write(file.getvalue())

        # # Now detect the format
        # detector = FileFormatDetector(temp_path)
        # detected_format = detector.detect_format()

        # print(f"Detected format for {file.name} is {detected_format}")
        
        # # Optionally remove the file if you no longer need it
        # os.remove(temp_path)