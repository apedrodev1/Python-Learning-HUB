"""
Handles the console output for displaying the list of students.

This module is responsible for printing a formatted, table-like report
of all students to the console.
"""

from ..utils.formatters import format_student_row_for_show

def display_students(student_list):
    """
    Displays the processed data of students in a readable table format.
    
    If the list is empty, it prints a "No students found" message.
    Otherwise, it prints a formatted header and then iterates over
    the list, printing one formatted row for each student.

    Args:
        student_list (list[Student]): A list of Student objects to be displayed.
        
    Returns:
        None
    """
    print("\n📊 Students Report:")

    if not student_list:
        print('❌ No students found.')
        return

    # Safe to access the first element now, as we've checked if the list is empty.
    type_label = "Weighted" if student_list[0].is_weighted else "Arithmetic"
    print(f"\n🧮 Average Calculation Type: {type_label}")

    print("─" * 100)
    print(f"{'ID':<5} {'Name':<20} {'Grades':<20} {'Average':<10} {'Status':<15} {'Passing Grade'}")
    print("─" * 100)

    for student in student_list:
        print(format_student_row_for_show(student))

    print("─" * 100)