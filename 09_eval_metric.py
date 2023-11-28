import csv
from collections import defaultdict

def read_csv_to_dict(file_path):
    data = defaultdict(list)
    with open(file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            file_path, line_numbers = row[0], row[1]
            data[file_path].extend(line_numbers.split('; '))
    return data

def calculate_metrics(true_labels, predictions):
    TP = sum(1 for file in predictions if file in true_labels and any(num in predictions[file] for num in true_labels[file]))
    FP = sum(1 for file in predictions if file not in true_labels or any(num not in true_labels[file] for num in predictions[file]))
    FN = sum(1 for file in true_labels if file not in predictions or any(num not in predictions[file] for num in true_labels[file]))

    precision = TP / (TP + FP) if (TP + FP) > 0 else 0
    recall = TP / (TP + FN) if (TP + FN) > 0 else 0
    f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
    modified_accuracy = TP / (TP + FP + FN) if (TP + FP + FN) > 0 else 0

    return precision, recall, f1, modified_accuracy


# File paths
true_label_path = '/workspaces/final_project/dataset/line_numbers_only.csv'
flawfinder_output_path = '/workspaces/final_project/dataset/flawfinder_output.csv'
rats_output_path = '/workspaces/final_project/dataset/rats_output.csv'

# Read data
true_labels = read_csv_to_dict(true_label_path)
flawfinder_predictions = read_csv_to_dict(flawfinder_output_path)
rats_predictions = read_csv_to_dict(rats_output_path)

# Calculate metrics
flawfinder_precision, flawfinder_recall, flawfinder_f1, flawfinder_accuracy = calculate_metrics(true_labels, flawfinder_predictions)
rats_precision, rats_recall, rats_f1, rats_accuracy = calculate_metrics(true_labels, rats_predictions)

# Print results
print(f"Flawfinder - Precision: {flawfinder_precision}, Recall: {flawfinder_recall}, F1 Score: {flawfinder_f1}, Accuracy: {flawfinder_accuracy}")
print(f"RATS - Precision: {rats_precision}, Recall: {rats_recall}, F1 Score: {rats_f1}, Accuracy: {rats_accuracy}")
