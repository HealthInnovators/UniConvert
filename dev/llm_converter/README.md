# LLMConverter

## Overview
The `LLMConverter` is a Python utility designed to utilize the capabilities of structured OpenAI models to process and convert natural language input into structured JSON data based on a predefined schema. It leverages the `superjsonmode.integrations.openai` module for interaction with OpenAI models and the `pydantic` module for defining and enforcing data types.

## Features
- Utilizes a structured OpenAI model to generate JSON data from natural language inputs.
- Incorporates schemas to define and validate the expected output format.
- Provides flexibility through customizable prompt templates.

## Usage Example

To use the `LLMConverter`, first ensure the necessary schema is defined and saved as a JSON file. Then, instantiate the converter and use it to process your input text.

```python
# Create an instance of LLMConverter with a schema file path
converter = LLMConverter("path_to_schema.json")

# Example input data
input_data = """Detailed description of a patient visit..."""

# Process the input to get structured output
structured_output = converter.convert(input_data)

# Output the structured JSON
print(structured_output)
