import re

def extract_cwe_and_line_info(output_text):
    # Regular expression to match each vulnerability block
    pattern = r'(/workspaces/final_project/dataset/.*?)(?=/workspaces/final_project/dataset/|ANALYSIS SUMMARY:)'
    blocks = re.findall(pattern, output_text, re.DOTALL)

    cwe_line_info = []
    for block in blocks:
        print(block)
        # Extract line number and CWE code from each block
        line_number_match = re.search(r':(\d+):', block)

        if line_number_match:
            line_number = line_number_match.group(1)
            # Extract all CWE codes in the block
            cwe_matches = re.findall(r'CWE-\d+', block)
            for cwe in cwe_matches:
                cwe_code = cwe.strip("()")
                cwe_line_info.append(f"{cwe_code}::{line_number}")

    return cwe_line_info


# Example output from flawfinder command
flawfinder_output = """
Flawfinder version 2.0.19, (C) 2001-2019 David A. Wheeler.
Number of rules (primarily dangerous function names) in C/C++ ruleset: 222
Examining /workspaces/final_project/dataset/000000014/Stack_overflow.c

FINAL RESULTS:

/workspaces/final_project/dataset/000000014/Stack_overflow.c:5:  [4] (buffer) strcpy:
  Does not check for buffer overflows when copying to destination [MS-banned]
  (CWE-120). Consider using snprintf, strcpy_s, or strlcpy (warning: strncpy
  easily misused).
/workspaces/final_project/dataset/000000014/Stack_overflow.c:4:  [2] (buffer) char:
  Statically-sized arrays can be improperly restricted, leading to potential
  overflows or other issues (CWE-119!/CWE-120). Perform bounds checking, use
  functions that limit length, or ensure that the size is larger than the
  maximum possible length.

ANALYSIS SUMMARY:

Hits = 2
Lines analyzed = 8 in approximately 0.00 seconds (3490 lines/second)
Physical Source Lines of Code (SLOC) = 5
Hits@level = [0]   0 [1]   0 [2]   1 [3]   0 [4]   1 [5]   0
Hits@level+ = [0+]   2 [1+]   2 [2+]   2 [3+]   1 [4+]   1 [5+]   0
Hits/KSLOC@level+ = [0+] 400 [1+] 400 [2+] 400 [3+] 200 [4+] 200 [5+]   0
Minimum risk level = 1

Not every hit is necessarily a security vulnerability.
You can inhibit a report by adding a comment in this form:
// flawfinder: ignore
Make *sure* it's a false positive!
You can use the option --neverignore to show these.

There may be other security vulnerabilities; review your code!
See 'Secure Programming HOWTO'
(https://dwheeler.com/secure-programs) for more information.
"""

# Extract the information
extracted_data = extract_cwe_and_line_info(flawfinder_output)
print(extracted_data)