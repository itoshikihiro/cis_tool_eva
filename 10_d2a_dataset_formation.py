import csv
import os

def process_d2a_dataset(csv_file_path, output_directory, label_csv_path):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    with open(csv_file_path, mode='r', encoding='utf-8') as file, \
         open(label_csv_path, mode='w', encoding='utf-8', newline='') as label_file:
        csv_reader = csv.DictReader(file)
        label_writer = csv.writer(label_file)
        label_writer.writerow(['id', 'label'])

        for row in csv_reader:
            function_code = row['functions'].strip("[]'")  # Strip list and quote characters
            function_code = function_code.replace('\\n', '\n')  # Replace literal \n with actual newlines
            function_code = function_code.replace('\\t', '\t')  # Replace literal \t with actual newlines
            file_id = row['id']
            label = row['label']

            # Write the function code to a .c file
            with open(os.path.join(output_directory, f"{file_id}.c"), mode='w', encoding='utf-8') as code_file:
                code_file.write(function_code)

            # Write the id and label to the label CSV
            label_writer.writerow([file_id, label])

# Define file paths
csv_file_path = '/workspaces/final_project/D2A/DAX_D2ALBData/code/d2a_lbv1_code_train.csv'
output_directory = '/workspaces/final_project/dataset_d2a'
label_csv_path = '/workspaces/final_project/dataset_d2a/label.csv'

# Process the dataset
process_d2a_dataset(csv_file_path, output_directory, label_csv_path)
