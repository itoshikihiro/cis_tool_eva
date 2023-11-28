import csv
import os

def list_files_in_directory(directory):
    # List all files in the given directory and its subdirectories
    file_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Construct the full file path
            full_path = os.path.join(root, file)
            # Normalize and add to the list
            normalized_path = os.path.normpath(full_path)
            file_paths.append(normalized_path)
    return file_paths

def filter_csv_by_directory(csv_file_path, directory, output_csv_path):
    # List all files in the directory
    existing_files = list_files_in_directory(directory)

    # Read and filter the CSV data
    filtered_data = []
    with open(csv_file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            # Construct the full path for the key from the CSV
            full_csv_path = os.path.normpath(os.path.join(directory, row[0]))
            if full_csv_path in existing_files:
                filtered_data.append(row)

    # Write the filtered data to a new CSV file
    with open(output_csv_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for row in filtered_data:
            writer.writerow(row)

# File paths
csv_file_path = '/workspaces/final_project/dataset/output.csv'
directory_to_check = '/workspaces/final_project/dataset'
filtered_csv_path = '/workspaces/final_project/dataset/filtered_output.csv'

# Filter the CSV file based on the directory contents
filter_csv_by_directory(csv_file_path, directory_to_check, filtered_csv_path)
