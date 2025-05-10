import json

def export_to_json(student_list, filename='students.json'):
    """
    Exports the student list to a JSON file.

    Args:
        student_list (list): List of Student instances.
        filename (str): File name to export.

    Returns:
        bool: True if export succeeded, False if skipped due to empty list.
    """
    if not student_list:
        print("⚠️  No students to export to JSON.")
        return False

    data = [student.to_dict() for student in student_list]
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"✅ Data successfully exported to {filename}")
    return True
