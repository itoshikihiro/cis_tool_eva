import csv
from collections import defaultdict

def read_csv_to_dict(file_path, is_evaluation=False):
    data = {}
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            key = row[0].replace('.c', '') if is_evaluation else row[0]
            data[key] = int(row[1])
    return data

def calculate_metrics(true_labels, predictions):
    TP = sum(1 for id, label in true_labels.items() if label == 1 and predictions.get(id) == 1)
    FP = sum(1 for id, label in true_labels.items() if label == 0 and predictions.get(id) == 1)
    FN = sum(1 for id, label in true_labels.items() if label == 1 and predictions.get(id) == 0)
    precision = TP / (TP + FP) if (TP + FP) > 0 else 0
    recall = TP / (TP + FN) if (TP + FN) > 0 else 0
    f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
    accuracy = (TP + (len(true_labels) - (TP + FP + FN))) / len(true_labels) if len(true_labels) > 0 else 0
    return precision, recall, f1, accuracy

# File paths
label_file = '/workspaces/final_project/dataset_d2a/label.csv'
flawfinder_output = '/workspaces/final_project/dataset_d2a/flawfinder_evaluation.csv'
rats_output = '/workspaces/final_project/dataset_d2a/rats_evaluation.csv'

# Read data
true_labels = read_csv_to_dict(label_file)
flawfinder_predictions = read_csv_to_dict(flawfinder_output, is_evaluation=True)
rats_predictions = read_csv_to_dict(rats_output, is_evaluation=True)

# Calculate metrics
flawfinder_metrics = calculate_metrics(true_labels, flawfinder_predictions)
rats_metrics = calculate_metrics(true_labels, rats_predictions)

# Print results
print(f"Flawfinder - Precision: {flawfinder_metrics[0]}, Recall: {flawfinder_metrics[1]}, F1 Score: {flawfinder_metrics[2]}, Accuracy: {flawfinder_metrics[3]}")
print(f"RATS - Precision: {rats_metrics[0]}, Recall: {rats_metrics[1]}, F1 Score: {rats_metrics[2]}, Accuracy: {rats_metrics[3]}")
