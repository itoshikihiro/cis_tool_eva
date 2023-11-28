import xml.etree.ElementTree as ET
import os

def parse_xml(xml_content):
    # Trim leading spaces and newlines
    xml_content = xml_content.strip()

    # Parse the XML
    root = ET.fromstring(xml_content)
    extracted_data = {}

    for testcase in root.findall('testcase'):
        file_element = testcase.find('file')
        if file_element is not None:
            # Extract path and modify it as per requirement
            path_parts = file_element.get('path').split('/')
            refined_path = ''.join(path_parts[:-1]) + '/' + path_parts[-1]
            refined_path = os.path.join("/workspaces/final_project/dataset", refined_path)
            
            # Extract flaws and format them
            flaws = []
            for flaw in file_element.findall('flaw'):
                flaw_name = flaw.get('name').split(' ')[0]  # Extract only CWE ID
                flaw_line = flaw.get('line')
                flaws.append(f"{flaw_name}:{flaw_line}")
            
            extracted_data[refined_path] = flaws

    return extracted_data

# Example XML content
xml_content = """
<?xml version="1.0" encoding="utf-8"?>
<container>
  <testcase id="4" type="Source Code" status="Candidate" submissionDate="2005-10-21" author="SecureSoftware" numberOfFiles="1" testsuiteid="17">
    <description><![CDATA[Miscalculated null termination occurs when the placement of a null character at
the end of a buffer of characters (or string) is misplaced or omitted. (from TCCLASP-5_2_14_9)]]></description>
    <file path="000/000/004/Miscalculated_null_termination.c" language="C" size="468" checksum="8bb66382fc751be505259593668886beb0eff30f">
      <flaw line="6" name="CWE-170: Improper Null Termination"/>
    </file>
  </testcase>
  <testcase id="5" type="Source Code" status="Candidate" submissionDate="2005-10-21" author="SecureSoftware" numberOfFiles="1">
    <description><![CDATA[Improper string length checking takes place when wide or multi-byte character
strings are mistaken for standard character strings. (from TCCLASP-5_2_15_10)]]></description>
    <file path="000/000/005/Improper_string_length_checking.c" language="C" size="453" checksum="f449e3214e8538773f2af2f982d1c1ae6a35aa21">
      <flaw line="11" name="CWE-133: String Errors"/>
    </file>
  </testcase>
  <testcase id="6" type="Source Code" status="Candidate" submissionDate="2005-10-26" author="SecureSoftware" numberOfFiles="1" testsuiteid="17">
    <description><![CDATA[The use of heap allocated memory after it has been freed or deleted leads to
undefined system behavior and, in many cases, to a write-what-where condition. (from TCCLASP-5_2_19_10)]]></description>
    <file path="000/000/006/Using_freed_memory.c" language="C" size="438" checksum="5d91ddf7a609b4c2490c245772b09d64c6960e0b">
      <flaw line="15" name="CWE-416: Use After Free"/>
      <flaw line="12" name="CWE-416: Use After Free"/>
    </file>
  </testcase>
</container>
"""

# Parse the XML and get the result
result = parse_xml(xml_content)
print(result)
