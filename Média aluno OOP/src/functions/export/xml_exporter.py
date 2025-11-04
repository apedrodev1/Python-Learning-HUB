"""
Provides the functionality to export student data to an XML file.

This module is called by the 'export_wrapper' and uses the
Student.to_dict() method to serialize data.
"""

import xml.etree.ElementTree as ET

def export_to_xml(student_list, filename='students.xml'):
    """
    Exports a list of Student objects to a specified XML file.

    It creates a root <students> element and a <student> element
    for each item in the list. The student's data is converted
    to sub-elements using the 'to_dict()' method.

    Args:
        student_list (list[Student]): The list of Student instances to export.
        filename (str, optional): The name of the file to create.
                                  Defaults to 'students.xml'.

    Returns:
        bool: True if the export was successful, False if the
              student list was empty.
    """
    if not student_list:
        print("⚠️  No students to export to XML.")
        return False

    root = ET.Element("students")

    for student in student_list:
        student_elem = ET.SubElement(root, "student")
        # Use the Student's to_dict() method to get serializable data
        for key, value in student.to_dict().items():
            child = ET.SubElement(student_elem, key)
            child.text = str(value)

    # Write the XML tree to the file
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)

    print(f"✅ Data successfully exported to {filename}")
    return True