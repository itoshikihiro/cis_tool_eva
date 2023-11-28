import csv
import os
import subprocess

def evaluate_rats(source_dir, output_csv_path):
    with open(output_csv_path, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['file_name', 'vulnerability_detected'])

        for file_name in os.listdir(source_dir):
            if file_name.endswith('.c'):
                file_path = os.path.join(source_dir, file_name)
                # Run rats
                cmd = f"rats -i {file_path}"
                process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, _ = process.communicate()

                # Check for vulnerabilities
                vulnerability_detected = stdout.decode().count(file_path) > 1
                writer.writerow([file_name, int(vulnerability_detected)])

# File paths
source_dir = '/workspaces/final_project/dataset_d2a'
output_csv_path = '/workspaces/final_project/dataset_d2a/rats_evaluation.csv'

# Evaluate rats
evaluate_rats(source_dir, output_csv_path)
