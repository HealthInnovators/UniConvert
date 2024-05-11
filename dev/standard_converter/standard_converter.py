import os
import json
import pandas as pd
import xmltodict
import yaml
# import xlrd
# import openpyxl


class FileConverter:
    def __init__(self, input_file_path, input_format, output_file_path, output_format):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.input_format = input_format.lower()
        self.output_format = output_format.lower()
        self.valid_formats = ['xml', 'yaml', 'csv', 'json', 'excel']
        self.name = "FileConverter"

    def __validate_inputs(self):
        if not os.path.exists(self.input_file_path):
            raise ValueError("Input file path does not exist.")

        # check if input file path is a file
        if not os.path.isfile(self.input_file_path):
            raise ValueError("Input file path is not a file.")

        # check if output file path's directory exists
        output_dir = os.path.dirname(self.output_file_path)

        if not os.path.exists(output_dir) and not output_dir == "":
            raise ValueError("Output file path's directory does not exist.")

        if self.input_format not in self.valid_formats:
            raise ValueError(f"Invalid input format. Valid formats are: {', '.join(self.valid_formats)}")

        if self.output_format not in self.valid_formats:
            raise ValueError(f"Invalid output format. Valid formats are: {', '.join(self.valid_formats)}")

        # check if input and output formats are the same
        if self.input_format == self.output_format:
            raise ValueError("Input and output formats are the same.")

        # # check if user has read permission for the input file
        # if not os.access(self.input_file_path, os.R_OK):
        #     raise PermissionError("You don't have permission to read the input file.")
        #
        # # check if user has write permission for the output file
        # output_dir = os.path.dirname(self.output_file_path)
        # if not os.access(output_dir, os.W_OK):
        #     raise PermissionError("You don't have permission to write to the output file's directory.")


    def convert_file(self):
        self.__validate_inputs()

        data = self.__read_file()

        print(data)
        exit()

        if data is None:
            return "Could not retrieve any data from the input file. Maybe the file is empty?"

        try:
            converted_data = self.__convert_data(data)
        except Exception as e:
            return f"Conversion failed. Error: {str(e)}"

        return self.__write_file(converted_data)

    def my_func(self):
        pass

    def __read_file(self):
        # Read the data from the input file based on its format
        class_name = self.__class__.__name__
        mangled_name = f"_{class_name}__read_as_{self.input_format}"
        reader_func = getattr(self, mangled_name, None)
        if reader_func:
            return reader_func()
        else:
            return None

    def __write_file(self, data):
        writer_func = getattr(self, f"__write_as_{self.output_format}", None)
        if writer_func:
            success = writer_func(data)
            if success:
                return "File conversion successful."
            else:
                return "File conversion failed."
        else:
            return "File conversion failed."

    def __convert_data(self, data):
        # Convert data to the desired output format
        converter_func = getattr(self, f"__convert_to_{self.output_format}", None)
        if converter_func:
            return converter_func(data)
        else:
            return None

    # Data reader functions for different formats
    def __read_as_xml(self):
        try:
            with open(self.input_file_path, 'r') as file:
                data = xmltodict.parse(file.read())
                return pd.json_normalize(data)
        except Exception as e:
            print(f"An error occurred while reading the XML file: {e}")
            return None

    def __read_as_yaml(self):
        try:
            with open(self.input_file_path, 'r') as file:
                data = yaml.safe_load(file)
                return pd.json_normalize(data)
        except Exception as e:
            print(f"An error occurred while reading the YAML file: {e}")
            return None

    def __read_as_csv(self):
        try:
            data = pd.read_csv(self.input_file_path)
            return data
        except Exception as e:
            print(f"An error occurred while reading the CSV file: {e}")
            return None

    def __read_as_json(self):
        try:
            with open(self.input_file_path, 'r') as file:
                data = json.load(file)
                return pd.json_normalize(data)
        except Exception as e:
            print(f"An error occurred while reading the JSON file: {e}")
            return None

    def __read_as_excel(self):
        try:
            pandas_excel = pd.ExcelFile(self.input_file_path)
            sheet_names = pandas_excel.sheet_names
            # Assuming there is only one sheet in the excel file. You can modify this based on your requirement
            data = pd.read_excel(pandas_excel, sheet_name=sheet_names[0])
            return data
        except Exception as e:
            print(f"An error occurred while reading the Excel file: {e}")
            return None

    def __write_as_csv(self, data):
        try:
            data.to_csv(f'{self.input_file_path}.csv', index=False)
            return True
        except Exception as e:
            print(f"Error occurred while writing CSV file: {str(e)}")
            return False

    def __write_as_json(self, data):
        try:
            with open(f'{self.input_file_path}.json', 'w') as file:
                json.dump(data, file, indent=2)
            return True
        except Exception as e:
            print(f"Error occurred while writing JSON file: {str(e)}")
            return False

    def __write_as_excel(self, data):
        try:
            writer = pd.ExcelWriter(f'{self.input_file_path}.xlsx')
            data.to_excel(excel_writer=writer, index=False)
            writer.save()
            return True
        except Exception as e:
            print(f"Error occurred while writing Excel file: {str(e)}")
            return False

    # Data conversion functions
    def __convert_to_xml(self, data):
        return data

    def __convert_to_yaml(self, data):
        return data

    def __convert_to_csv(self, data):
        if isinstance(data, dict):
            # If the data is a dictionary, convert it to a dataframe and then convert to csv
            data = pd.DataFrame.from_dict(data)
        return data

    def __convert_to_json(self, data):
        if isinstance(data, pd.DataFrame):
            # If the data is a dataframe, convert it to a dictionary and then convert to json
            data = data.to_dict(orient='records')
        return data

    def __convert_to_excel(self, data):
        if isinstance(data, dict):
            # If data is dictionary, convert it to a dataframe
            data = pd.DataFrame.from_dict(data)
        return data


# Example usage:
if __name__ == "__main__":
  input_file_path = "test6.yaml"
  output_file_path = "converted_sample_data.json"
  # Converting from XML to JSON
  converter = FileConverter(input_file_path, "yaml", output_file_path, "json")
  result = converter.convert_file()
  print(result)
