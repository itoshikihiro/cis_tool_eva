import re

def extract_flawfinder_line_info(output_text):
    # Regular expression to match line numbers
    pattern = r'(\.c):(\d+):'
    line_number_matches = re.findall(pattern, output_text)

    # Extract line numbers
    line_numbers = [match[1] for match in line_number_matches]

    return line_numbers

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

# Extract line number information
extracted_info = extract_flawfinder_line_info(flawfinder_output)
print(extracted_info)
