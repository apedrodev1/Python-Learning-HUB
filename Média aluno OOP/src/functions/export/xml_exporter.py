import xml.etree.ElementTree as ET

def export_to_xml(student_list, filename='students.xml'):
    """
    Exports the student list to an XML file.

    Args:
        student_list (list): List of Student instances.
        filename (str): File name to export.

    Returns:
        bool: True if export succeeded, False if skipped due to empty list.
    """
    if not student_list:
        print("⚠️  No students to export to XML.")
        return False

    root = ET.Element("students")

    for student in student_list:
        student_elem = ET.SubElement(root, "student")
        for key, value in student.to_dict().items():
            child = ET.SubElement(student_elem, key)
            child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)

    print(f"✅ Data successfully exported to {filename}")
    return True
