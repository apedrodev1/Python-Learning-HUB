"""
Presents the user with export format options (JSON or XML).

This module acts as a simple wrapper or router that displays a
console menu and calls the corresponding exporter function
(json_exporter or xml_exporter) based on user input.
"""

from .json_exporter import export_to_json
from .xml_exporter import export_to_xml

def export_students(student_list):
    """
    Handles user choice for exporting data (JSON or XML).

    If the student list is empty, this function will print a message
    and exit. Otherwise, it will loop until the user selects a valid
    export format (1 for JSON, 2 for XML) or skips (0).

    Args:
        student_list (list[Student]): The list of Student objects to export.
    
    Returns:
        None
    """
    if not student_list:
        print("⚠️  No students to export.")
        return

    while True:
        print("\n 🖨️  Export Options:")
        print("1 - Export to JSON")
        print("2 - Export to XML")
        print("0 - Skip export\n")

        choice = input("Choose export format: ")

        if choice == "1":
            export_to_json(student_list)
            break
        elif choice == "2":
            export_to_xml(student_list)
            break
        elif choice == "0":
            print("ℹ️  Export skipped.")
            break
        else:
            print("❌ Invalid choice. Please choose 1, 2, or 0.")