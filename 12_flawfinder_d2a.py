import csv
import os
import subprocess

def evaluate_flawfinder(source_dir, output_csv_path):
    with open(output_csv_path, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['file_name', 'vulnerability_detected'])

        for file_name in os.listdir(source_dir):
            if file_name.endswith('.c'):
                # Run flawfinder
                cmd = f"flawfinder {os.path.join(source_dir, file_name)}"
                process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, _ = process.communicate()

                # Check for vulnerabilities
                vulnerability_detected = 'No hits found' not in stdout.decode()
                writer.writerow([file_name, int(vulnerability_detected)])

# File paths
source_dir = '/workspaces/final_project/dataset_d2a'
output_csv_path = '/workspaces/final_project/dataset_d2a/flawfinder_evaluation.csv'

# Evaluate flawfinder
evaluate_flawfinder(source_dir, output_csv_path)
