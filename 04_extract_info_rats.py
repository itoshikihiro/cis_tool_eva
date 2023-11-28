import re

def extract_rats_line_info(output_text):
    # Regular expression to match each vulnerability block
    pattern = r'(/workspaces/final_project/dataset/.*?)(?=/workspaces/final_project/dataset/|Total lines analyzed:)'
    blocks = re.findall(pattern, output_text, re.DOTALL)

    line_info = []
    for block in blocks:
        # Extract line number
        line_number_match = re.search(r':(\d+):', block)
        if line_number_match:
            line_number = line_number_match.group(1)
            line_info.append(line_number)

    return line_info

# Example output from rats command
rats_output = """
Entries in perl database: 33
Entries in ruby database: 46
Entries in python database: 62
Entries in c database: 334
Entries in php database: 55
Analyzing /workspaces/final_project/dataset/000000014/Stack_overflow.c
/workspaces/final_project/dataset/000000014/Stack_overflow.c:4: High: fixed size local buffer
Extra care should be taken to ensure that character arrays that are allocated
on the stack are used safely.  They are prime targets for buffer overflow
attacks.

/workspaces/final_project/dataset/000000014/Stack_overflow.c:5: High: strcpy
Check to be sure that argument 2 passed to this function call will not copy
more data than can be handled, resulting in a buffer overflow.

Total lines analyzed: 9
Total time 0.001851 seconds
4862 lines per second
"""

# Extract line number information
extracted_info = extract_rats_line_info(rats_output)
print(extracted_info)
