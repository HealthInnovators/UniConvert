import os
import csv

def generate_csv(directory_path):
    csv_data = []
    header = ['Address', 'Empty', 'Wrong_Extension?', 'Given_Extension', 'Actual_Extension', 'Faulty?']

    for file_name in os.listdir(directory_path):
        full_path = os.path.join(directory_path, file_name)
        base_name, extension = os.path.splitext(file_name)
        
        # Checking Empty
        is_empty = 'empty' in file_name.lower()
        
        # Checking Wrong_Extension?
        is_wrong_ext = 'fake' in base_name.lower()

        # Checking Faulty?
        is_faulty = 'faulty' in file_name.lower()

        # Getting Actual_Extension
        actual_extension = extension[1:]
        if is_wrong_ext:
            actual_extension = base_name.split('_fake_')[1].split('.')[-1]

        csv_data.append([
            full_path, 
            is_empty, 
            is_wrong_ext,
            extension[1:],
            actual_extension,
            is_faulty
        ])

    # Sort the csv_data list in alphabetical order using file name
    csv_data.sort(key = lambda x: x[0])

    with open('file_details.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(csv_data)

# Replace 'your_directory_path' with the actual directory path
generate_csv('data/')
