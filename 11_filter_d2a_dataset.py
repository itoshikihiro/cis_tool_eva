import csv
import os
import shutil

def process_dataset(source_dir, label_file, dest_dir, new_label_file):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Read labels into a set
    labeled_ids = set()
    with open(label_file, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            labeled_ids.add(row[0])

    # Process source files and update labels
    with open(new_label_file, mode='w', encoding='utf-8', newline='') as label_out:
        writer = csv.writer(label_out)
        writer.writerow(['id', 'label'])

        for file in os.listdir(source_dir):
            if file.endswith('.c'):
                file_id = os.path.splitext(file)[0]
                if file_id in labeled_ids:
                    # Move file to new directory
                    shutil.move(os.path.join(source_dir, file), os.path.join(dest_dir, file))
                    # Write label to new label file
                    writer.writerow([file_id])

# File paths
source_dir = '/workspaces/final_project/dataset_d2a'
label_file = '/workspaces/final_project/dataset_d2a/label.csv'
dest_dir = '/workspaces/final_project/dataset_d2a_v2'
new_label_file = '/workspaces/final_project/dataset_d2a_v2/label.csv'

# Process the dataset
process_dataset(source_dir, label_file, dest_dir, new_label_file)
