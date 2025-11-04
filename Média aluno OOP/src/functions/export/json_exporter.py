"""
Provides the functionality to export student data to a JSON file.

This module is called by the 'export_wrapper' and uses the
Student.to_dict() method to serialize data.
"""

import json

def export_to_json(student_list, filename='students.json'):
    """
    Exports a list of Student objects to a specified JSON file.

    It serializes the list of Student objects by calling the 'to_dict()'
    method on each one, and then dumps the resulting list into a
    formatted JSON file.

    Args:
        student_list (list[Student]): The list of Student instances to export.
        filename (str, optional): The name of the file to create.
                                  Defaults to 'students.json'.

    Returns:
        bool: True if the export was successful, False if the
              student list was empty.
    """
    if not student_list:
        print("⚠️  No students to export to JSON.")
        return False

    # Create a list of dictionaries using the Student.to_dict() method
    data = [student.to_dict() for student in student_list]
    
    # Write the data to the JSON file
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"✅ Data successfully exported to {filename}")
    return True