import csv
import subprocess
import re

def run_tool_and_extract_line_numbers(file_path):
    # Run flawfinder on the given file path
    cmd = f"flawfinder {file_path}"
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    # Extract line numbers from the output
    output_text = stdout.decode()
    line_numbers = re.findall(r':(\d+):', output_text)
    return line_numbers

def process_csv_file(input_csv_path, output_csv_path):
    processed_data = {}

    with open(input_csv_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            file_path = row[0]
            line_numbers = run_tool_and_extract_line_numbers(file_path)
            processed_data[file_path] = line_numbers

    # Write the processed data to a new CSV file
    with open(output_csv_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for key, value in processed_data.items():
            writer.writerow([key, '; '.join(value)])

# File paths
input_csv_file_path = '/workspaces/final_project/dataset/line_numbers_only.csv'
output_csv_file_path = '/workspaces/final_project/dataset/flawfinder_output.csv'

# Process the CSV file and run the tools
process_csv_file(input_csv_file_path, output_csv_file_path)
