import xml.etree.ElementTree as ET
import csv
import os

def parse_xml(xml_file_path):
    # Read the XML file
    with open(xml_file_path, 'r', encoding='utf-8') as file:
        xml_content = file.read()

    # Parse the XML
    root = ET.fromstring(xml_content)
    extracted_data = {}

    for testcase in root.findall('testcase'):
        file_element = testcase.find('file')
        if file_element is not None:
            path_parts = file_element.get('path').split('/')
            refined_path = ''.join(path_parts[:-1]) + '/' + path_parts[-1]
            refined_path = os.path.join("/workspaces/final_project/dataset", refined_path)
            flaws = [f"{flaw.get('name').split(' ')[0]}:{flaw.get('line')}" for flaw in file_element.findall('flaw')]
            extracted_data[refined_path] = flaws

    return extracted_data

def write_to_csv(data, csv_file_path):
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for key, value in data.items():
            writer.writerow([key, '; '.join(value)])

# File paths
xml_file_path = '/workspaces/final_project/dataset/SARD_testcaseinfo.xml'
csv_file_path = '/workspaces/final_project/dataset/output.csv'

# Parse the XML and write to CSV
data = parse_xml(xml_file_path)
write_to_csv(data, csv_file_path)
