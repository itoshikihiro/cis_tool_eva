import csv
import re

def process_csv_to_include_only_line_numbers(csv_file_path, output_csv_path):
    processed_data = {}
    
    # Read the CSV file
    with open(csv_file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            file_path = row[0]
            # Extract line numbers from the vulnerability info
            line_numbers = re.findall(r'::(\d+)', row[1])
            processed_data[file_path] = line_numbers

    # Write the processed data to a new CSV file
    with open(output_csv_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for key, value in processed_data.items():
            writer.writerow([key, '; '.join(value)])

# File paths
original_csv_file_path = '/workspaces/final_project/dataset/filtered_output.csv'
new_csv_file_path = '/workspaces/final_project/dataset/line_numbers_only.csv'

# Process the CSV file
process_csv_to_include_only_line_numbers(original_csv_file_path, new_csv_file_path)
